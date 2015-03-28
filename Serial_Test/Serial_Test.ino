void setup() {
  Serial.begin(9600);
  myservo.attach(6);
  
}

void loop() {
  if (Serial.available() > 0) 
  {
    incomingByte = Serial.read();
  }
  Serial.println(char(incomingByte));
}
