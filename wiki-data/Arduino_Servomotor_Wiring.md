1.  Arduino Servomotor Wiring

`== Code ==`\
\
`#include `<Servo.h>\
\
`Servo myservo;  // create servo object to control a servo`\
\
` // twelve servo objects can be created on most boards`\
\
` int pos = 90;    // variable to store the servo position`\
` `\
` int pinPulse = 8;`\
\
`void setup() {`\
\
` myservo.attach(3);  // attaches the servo on pin 9 to the servo object`\
\
` pinMode (pinPulse, OUTPUT);`\
\
` Serial.begin (9600); `\
\
`}`\
\
`void loop() {`\
\
`  for (pos = 90; pos <= 110; pos += 1) { // goes from 90 degrees to 180 degrees`\
\
`   // in steps of 1 degree`\
\
`   myservo.write(pos);              // tell servo to go to position in variable 'pos'`\
\
`   delay(1000);                         // waits 5ms for the servo to reach the position`\
\
`   digitalWrite(pinPulse, HIGH);`\
\
`//   delayMicroseconds (5);           //delay 2.5us`\
\
`    digitalWrite(pinPulse, LOW);`\
`  }`\
\
`  `\
`  for (pos = 110; pos >= 90; pos -= 1) { // goes from 180 degrees to 0 degrees\`\
\
`    myservo.write(pos);              // tell servo to go to position in variable 'pos'`\
\
`    delay(1000);                       // waits 5ms for the servo to reach the position`\
\
`    digitalWrite(pinPulse, HIGH);`\
\
` //  delayMicroseconds (5);           //delay 2.5us  `\
\
`   digitalWrite(pinPulse, LOW);`\
\
`  }`\
`  `\
`}`\
\
\

<Category:Motor> <Category:electrionics>
