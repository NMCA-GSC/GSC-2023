#include <SD.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(9, 8); // RX, TX pins for Bluetooth module
File myFile;

void setup() {
  Serial.begin(9600);
  bluetoothSerial.begin(9600);

  if (!SD.begin(4)) {
    Serial.println("SD card initialization failed!");
    return;
  }

  myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("File opened successfully");
  } else {
    Serial.println("Error opening file");
  }
}

void loop() {
  if (bluetoothSerial.available()) {
    char command = bluetoothSerial.read();
    if (command == 'S') { // 'S' indicates a request to send the file
      sendFile();
      command=' '; //reset command indicator
    }
  }
}

void sendFile() {
  if (myFile) {
    while (myFile.available()) {
      char data = myFile.read();
      bluetoothSerial.write(data);
    }
    bluetoothSerial.write("\n");
    Serial.println("File sent successfully");
    while (1); // Stop further execution, or add your own logic
  } else {
    Serial.println("Error reading file");
  }
}
