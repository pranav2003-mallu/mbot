#ifndef ENCODER_DRIVER_H
#define ENCODER_DRIVER_H

// Arduino-compatible pin numbers for Pi Pico
#define LEFT_ENC_PIN_A 14
#define LEFT_ENC_PIN_B 15

#define RIGHT_ENC_PIN_A 16
#define RIGHT_ENC_PIN_B 17

long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();
void initEncoders();

#endif
