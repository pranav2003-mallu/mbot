#ifndef MOTOR_DRIVER_H
#define MOTOR_DRIVER_H

// MDD20A Dual Channel Motor Driver
// Left Motors Channel (M1)
#define LEFT_PWM 2  // PWM 1
#define LEFT_DIR 3  // DIR 1

// Right Motors Channel (M2)
#define RIGHT_PWM 8 // PWM 2
#define RIGHT_DIR 9 // DIR 2

void initMotorController();
void setMotorSpeed(int i, int spd);
void setMotorSpeeds(int leftSpeed, int rightSpeed);

#endif
