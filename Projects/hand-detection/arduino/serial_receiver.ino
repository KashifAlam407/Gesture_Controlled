// This is the arduino code first you have to upload it to your arduino then run python code 

#include <Servo.h>

Servo thumb, index, middle, ring, pinky;

void setup() {
  Serial.begin(115200);

  thumb.attach(3);    // attach thumb to pin 3 of arduino
  index.attach(5);   // attach thumb to pin 5 of arduino
  middle.attach(6);   // attach thumb to pin 6 of arduino
  ring.attach(9);    // attach thumb to pin 9 of arduino
  pinky.attach(10);    // attach thumb to pin 10 of arduino

  // I have set the value of my servo angle according to my fingers postion you have to set according to your fingers
  thumb.write(150);    
  index.write(0);
  middle.write(0);
  ring.write(120);
  pinky.write(140);

}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); // e.g., "01100"
    if (data.length() == 5) {
      thumb.write(data[0]=='1'?150:0);
      index.write(data[1]=='1'?0:140);
      middle.write(data[2]=='1'?0:120);
      ring.write(data[3]=='1'?120:0);
      pinky.write(data[4]=='1'?140:0);
    }
  }

}


