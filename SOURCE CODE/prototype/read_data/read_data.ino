#include <EEPROM.h>

void setup() {
  Serial.begin(9600);
  char myString[] = "Hello World\n"
  
  ;
  EEPROM.put(0, myString);
}

void loop() {
  // put your main code here, to run repeatedly:
  char data;
  int address = 0;

  // Read and print each character until a null character is encountered
  while (1) {
    EEPROM.get(address, data);
    if (data == '\0') {
      break; // Exit loop when null character is encountered
    }
    Serial.print(data);
    address++;
  }

  delay(1000); // Add a delay to see the output
}
