#include "Arduino.h"
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>

const byte rxPin = 9;
const byte txPin = 8;
SoftwareSerial BTSerial(rxPin, txPin); // RX TX
String incomingData ;
File myFile;

void setup() {
  // define pin modes for tx, rx:
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  BTSerial.begin(9600);
  Serial.begin(9600);
  if (!SD.begin(4)) {
    Serial.print("Initialization Failed");
    while(1);
  }
  else {
    Serial.print("Initialization Complete");
  }
}

void loop() {
  while (BTSerial.available() > 0) {
    incomingData = BTSerial.readStringUntil('\4');
    SD.remove("test.txt");
    myFile = SD.open("test.txt", FILE_WRITE);
    if (myFile) {
      myFile.
      myFile.print(incomingData);
      myFile.close();
    }
    else {
      Serial.print("No file to open");
    }
    }
  }