#include "Arduino.h"
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>

const byte rxPin = 9;
const byte txPin = 8;
SoftwareSerial BTSerial(rxPin, txPin); // RX TX
File myFile;

const int MAX_BUFFER_SIZE = 256;  // Adjust this value based on your needs

void setup() {
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  BTSerial.begin(9600);
  Serial.begin(9600);

  if (!SD.begin(4)) {
    Serial.println("Initialization Failed!");
    while(1);
  } else {
    Serial.println("Initialization Complete");
  }
}

void loop() {
  static String incomingData;
  while (BTSerial.available() > 0) {
    char incomingChar = BTSerial.read();

    if (incomingChar == '\n') {
      // Newline character received, process the complete string
      writeFile("test.txt", incomingData);
      incomingData = "";  // Reset the string for the next iteration
    } else {
      // Accumulate characters until newline is received
      incomingData += incomingChar;

      // Limit the size of the buffer
      if (incomingData.length() >= MAX_BUFFER_SIZE) {
        Serial.println("Error: Incoming data exceeds buffer size");
        incomingData = "";  // Reset the string to avoid overflow
      }
    }
  }
}

void writeFile(const char* fileName, const String& data) {
  myFile = SD.open(fileName, FILE_WRITE);

  if (myFile) {
    myFile.print(data);
    myFile.close();
  } else {
    Serial.println("Error opening file");
  }
}
