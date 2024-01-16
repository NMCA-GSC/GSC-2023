/*###########################################################

                    NMCA GSC LISCENSE
            Copyright (c) <year> Authors.txt
        See full license in attached license.md

    The code contained below is a covered in full as 
    part of the entity as defined in the license and
    it's stated admendments. No warranty or liability 
    is claimed for the use of this code, which is 
    provided on an AS-IS BASIS. 

###########################################################*/

#include "WRITE_FILE.h"

const int MAX_BUFFER_SIZE = 256;
extern SoftwareSerial BTSerial;
File myFile;

void WRITE_FILE::writeFile() {
  static String incomingData;
  unsigned long startTime = millis();  // Record the start time
  
  while (millis() - startTime < 1000) {  // Adjust the timeout as needed (1 second in this example)
    if (BTSerial.available() > 0) {
      char incomingChar = BTSerial.read();

      if (incomingChar == '\n') {
        // Newline character received, process the complete string
        myFile = SD.open("test.txt", FILE_WRITE);

        if (myFile) {
          myFile.print(incomingData); // Use println to automatically append newline
          myFile.close();
        } else {
          Serial.println("Error opening file");
        }

        incomingData = "";  // Reset the string for the next iteration
        startTime = millis();  // Reset the timer for the next iteration
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
}
