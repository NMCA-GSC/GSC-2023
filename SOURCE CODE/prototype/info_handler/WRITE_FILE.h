#ifndef WRITE_FILE_H
#define WRITE_FILE_H

#include "Arduino.h"
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>

class WRITE_FILE {
public:
  void writeFile();
};

extern File myFile;  // Declare myFile as an external variable

#endif // WRITE_FILE_H
