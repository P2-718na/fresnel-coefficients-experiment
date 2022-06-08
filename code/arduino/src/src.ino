#define sensorPin A0

int sensorValue = 0;
int delayTime = 500; // Delay between consecutive acquisitions

int state = -1;
int count = 0;

void readSensorAndPrint() {
  // Read (uncorrected) sensor value
  sensorValue = analogRead(sensorPin);

  // Correct sensor value by comparing it to Vref.
  // Numbers output from this will be in range [0, 1024].
  sensorValue = (float)readVcc() * (float)sensorValue / 1000.f / 5.f;

  Serial.println(sensorValue);

  delay(delayTime);
}

void parseCommand() {
  String cmd = Serial.readStringUntil(' ');
  String val = Serial.readStringUntil('\n');

  if (cmd == "loop") {
    state = 0;
    return;
  }

  if (cmd == "delay") {
    delayTime = val.toInt();
    return;
  }

  if (cmd == "acq") {
    Serial.println("Beginning acquisition...");
    state = 1;
    count = val.toInt();
    return;
  }

  if (cmd == "clear") {
    state = 2;
    return;
  }

   if (cmd == "stop") {
    state = -1;
    return;
  }
}

// see: https://www.youtube.com/watch?v=xI_qU2auVx8
// and: https://forum.arduino.cc/t/how-to-know-vcc-voltage-in-arduino/344001/4
// This uses ADC to read VREF.
long readVcc() {
  long result;
  // Read 1.1V reference against Vcc, then use the result to calculate the actual Vcc value.
  # define ADMUX = _BV(REFS0) | _BV(MUX4) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);

  delay(2); // Wait for Vref to settle

  ADCSRA |= _BV(ADSC); // Convert
  while (bit_is_set(ADCSRA, ADSC));
  result = ADCL;
  result |= ADCH << 8;
  result = 1126400L / result; // Calculate Vcc (in mV); 1126400 = 1.1*1024*1000 (need to / measured)

  return result;
}

void setup() {
  // Please note that opening/closing a serial communication from the other end resets the board.
  // See https://forum.arduino.cc/t/look-like-arduino-reboot-when-open-and-close-serial-monitor/362206/3
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    parseCommand();
  }

  switch (state) {
    case 0:
      readSensorAndPrint();
      break;

    case 1:
      while (count --> 0) {
        readSensorAndPrint();
      }
      Serial.println("Acquisition complete!");
      state = -1;
      break;

     case 2:
      for (count = 500; count --> 0;) {
        Serial.println("0");
      }
      state = -1;
      break;

    default:
      break;
  }
}
