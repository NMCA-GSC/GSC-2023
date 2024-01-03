String incomingByte ;    

void setup() {

  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);

}
void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');
    Serial.write(incomingByte.c_str());

  }

}

