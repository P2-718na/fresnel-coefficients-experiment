import serial
import numpy as np
import requests
from time import sleep
from sys import argv

if len(argv) != 3:
    print("Usage: py daq.py arduino-port monitor-port")
    exit(1)

arduino = serial.Serial(port=argv[1], baudrate=115200, timeout=100)  # Physical arduino port
monitor = serial.Serial(port=argv[2], baudrate=115200, timeout=100)  # Port to forward data to

# Wait for arduino to reset...
sleep(2)

# Local variables...
points = {}
data = []
step_size = 2


# Acquire n samples.
def acq(num_samples):
    samples = []
    arduino.flushInput()
    arduino.flushOutput()

    # Check that arduino is not in loop mode...
    assert b"Beginning acquisition..." in arduino.readline()

    for i in range(int(num_samples)):
        line = arduino.readline()
        samples.append(int(line))

    assert b"Acquisition complete!" in arduino.readline()

    return samples, np.std(samples), np.mean(samples)


def main():
    global step_size
    global points
    global data

    while True:
        cmd = input(">")

        # Read data continuously
        # Usage: loop
        if "loop" in cmd:
            arduino.write(b"loop \n")
            try:
                while True:
                    line = arduino.readline()
                    print(line.decode("utf8").strip())
                    monitor.write(line)

            except KeyboardInterrupt:
                arduino.write(b"stop \n")
                arduino.flushInput()
                arduino.flushOutput()
                continue
            continue

        # Change stepper motor step size.
        # Usage: stepsize n
        if "stepsize" in cmd:
            step_size = int(cmd.split(" ")[1])

        # Acquire n samples without saving to memory.
        # Usage: acq n
        if "acq" in cmd:
            arduino.write(cmd.encode() + b"\n")
            data, std, mean = acq(int(cmd.split(" ")[1]))
            print(data, std, mean)
            continue

        # Acquire n samples, save them to memory and move stepper motor.
        # Usage: take n
        if "take" in cmd:
            num_samples = int(cmd.split(" ")[1])
            arduino.write(b"acq " + str(num_samples).encode() + b"\n")
            _, std, mean = acq(num_samples)

            theta = int(requests.get("http://192.168.4.1/virtual").text)
            print("New sample with angle:", theta)

            points[str(90 - theta)] = {
                "I": mean * 100 // 1 / 100,
                "delta_I": std * 100 // 1 / 100,
                "delta_theta": 0.5
            }

            headers_ = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            requests.post("http://192.168.4.1/move", data="distance=" + str(step_size), headers=headers_)
            print("Stepping", step_size, "degree(s)...")
            continue

        # Display data in memory
        # Usage: disp
        if "disp" in cmd:
            print(points)
            continue

        # Move forward n steps. Use a negative n value to move backwards.
        # Usage: move n
        if "move" in cmd:
            headers_ = {
              "Content-Type": "application/x-www-form-urlencoded"
            }
            requests.post("http://192.168.4.1/move", data="distance=" + cmd.split(" ")[1], headers=headers_)
            continue

        # Write to file data stored in memory.
        # Usage: write
        if "write" in cmd:
            with open("data.txt", "w") as file:
                for theta, point in points.items():
                    file.write(f"{theta} {point['I']} {point['delta_theta']} {point['delta_I']}\n")
            continue

        # All unknown commands will be forwarded to the Arduino.
        # !Please make sure to add a trailing space if the command is made up
        # of a single word!
        arduino.write(cmd.encode() + b"\n")


main()
