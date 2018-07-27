int sum = 0;
int sample_count = 0;
double voltage = 0.0;

void setup() {
 Serial.begin(9600);
}

void loop() {
Serial.println(analogRead(A2));
/*
  while(sample_count < 10){
    sum += analogRead(A2);
    sample_count++;
    delay(10);
  }

  voltage = ((double)sum/10.0 * 5.015)/1024.0;
  Serial.println(voltage * 11.132);
  sum = 0;
  sample_count = 0;
  */
  /*
  float sensorValue = analogRead(A2);
  float voltage = map(sensorValue,0,1024,0,2500);
  voltage/=100;

  //for (int )
  
  Serial.println(sensorValue);
  Serial.print("Voltage:");
  Serial.println(voltage);
  delay(500);*/
}
