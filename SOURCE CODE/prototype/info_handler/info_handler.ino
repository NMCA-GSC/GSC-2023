#include "WRITE_FILE.h"

WRITE_FILE writefile;
SoftwareSerial BTSerial(9, 8); // RX TX

void setup() {
  pinMode(9, INPUT);
  pinMode(8, OUTPUT);
  BTSerial.begin(9600);
  Serial.begin(9600);

  if (!SD.begin(4)) {
    Serial.println("Initialization Failed!");
    return;
  } else {
    Serial.println("Initialization Complete");
  }
}

void loop() {
  while (BTSerial.available() > 0) {
    char cmdChar = BTSerial.read();
    if (cmdChar == 'R') {
      Serial.print("receieving...");
      writefile.writeFile(); 
      Serial.println("Done");
    } else if (cmdChar == 'S') {
      Serial.print("Sending...");
      sendFile();
      cmdChar = '\0';
      Serial.println("Done");
    }
  }
}

void sendFile() {
  File myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("File opened successfully");
    
    while (myFile.available()) {
      char data = myFile.read();
      BTSerial.write(data);
    }
    BTSerial.write('\n');
    Serial.println("File sent successfully");
  } else {
    Serial.println("Error opening file");
  }
  myFile.close();
}
