// program makes the robot avoid obstacles while moving moving forward
#include <adafruit_neopixel.h>

#define PIN 2
#define NUM_LEDS 1

//left motor
#define motor11 5
#define motor12 3

//right motor
#define motor21 9
#define motor22 6

//sensor variables
#define left_sensor 14
#define right_sensor 8

int l1=0;
int r1=0;

Adafruit_NeoPixel strip=Adafruit_NeoPixel(NUM_LEDS,PIN<NEO_GRB+NEO_KHZ800);

void setup()
{
    PinMode(motor11,OUTPUT);
    PinMode(motor12,OUTPUT);
    PinMode(motor21,OUTPUT);
    PinMode(motor22,OUTPUT);


Serial.begin(9600);
Strip,set Brightness(80);
Strip.setPixelcolor(0,0,0,150);
Strip.show();
}
voidloop()
{
    obstracle Avoidance();
}

    void obstracle Avoidance()
{
    SerialPrintln("obstacle Avoidance");
    l1=digital Read(Left_Sensor);
    r1=digital Read(Right_Sensor);
    Serial.print(l1);
    Serial.print("\t");
    Serial.print(r1);

// Turning right when object on left
if(l1==LOW && r1==HIGH)
{
    analogWrite(motor11,150);
    analogWrite(motor12,0);
    analogWrite(motor21,0);
    analogWrite(motor22,150);

}
// Turning LEFT when object on RiGHT
elseif(l1==HIGH && r1==LOW)
{
    analogWrite(motor11,0);
    analogWrite(motor12,150);
    analogWrite(motor21,150);
    analogWrite(motor22,0);

}
// Continuing on a straight path when object on RiGHT
elseif(l1==HIGH && r1==HIGH)
{
    analogWrite(motor11,150);
    analogWrite(motor12,0);
    analogWrite(motor21,150);
    analogWrite(motor22,0);

}
// IF object on RiGHT  HEAD
if(l1==LOW && r1==LOW)
{
// go back
    analogWrite(motor11,0);
    analogWrite(motor12,150);
    analogWrite(motor21,0);
    analogWrite(motor22,150);
delay(600);
//turn right
analogWrite(motor11,0);
analogWrite(motor12,150);
analogWrite(motor21,150);
analogWrite(motor22,0);
delay(1400);
}
}
rfhvhggh