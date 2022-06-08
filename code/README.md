# Code
This folder contains all the code we used.

- 📁 [arduino](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/code/arduino)
  - Code uploaded on the Arduino board.
- 📁 [daq](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/code/daq)
  - Python script used to acquire data. See below for running instructions.
- 📁 [esp32](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/code/esp32)
  - We don't talk about this code.
- 📁 [fitting](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/code/fitting)
  - Code used to fit data (different variants) and to compute chi square.
- 📁 [graphs](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/code/esp32)
  - Code used to generate graphs. See below for running instructions.

## Running daq
1) Create two connected virtual serial ports:
   ```bash
   socat -d -d pty,raw,echo=0 pty,raw,echo=0
   ```
2) Pipe the output of one port to `ttyplot` (install it first):
   ```bash
   cat /dev/socat_port_name_2 | ttyplot
   ```
3) Run
   ```bash
   py daq.py /dev/arduino_port_name /dev/socat_port_name_1
   ```

## Building graphs
1) `cd` to repository root directory and run
   ```bash
   pipenv run build:graphs
   ```
   to generate graphs.
2) Graphs will be generated in the `build` folder.
