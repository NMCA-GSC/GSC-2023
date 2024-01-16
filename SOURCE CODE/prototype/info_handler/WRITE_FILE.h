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
