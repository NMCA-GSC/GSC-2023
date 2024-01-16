#include "Arduino.h"
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>

const byte rxPin = 9;
const byte txPin = 8;
SoftwareSerial BTSerial(rxPin, txPin); // RX TX
File myFile;

const int MAX_BUFFER_SIZE = 256;  // Adjust this value based on your needs

void writeFile() {
  static String incomingData;
  while (BTSerial.available() > 0) {
    char incomingChar = BTSerial.read();

    if (incomingChar == '\n') {
      // Newline character received, process the complete string
      myFile=SD.open("test.txt", FILE_WRITE);
      if (myFile) {
        myFile.print(incomingData);
        myFile.close();
      } else {
        Serial.println("Error opening file");
      }
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