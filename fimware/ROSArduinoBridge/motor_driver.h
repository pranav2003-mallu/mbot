/***************************************************************
   Motor driver function definitions - by James Nugen
   *************************************************************/


#ifdef MDD20A_MOTOR_DRIVER
  #define RIGHT_MOTOR_PWM 5
  #define RIGHT_MOTOR_DIR 6
  #define LEFT_MOTOR_PWM 9
  #define LEFT_MOTOR_DIR 10
#endif

void initMotorController();
void setMotorSpeed(int i, int spd);
void setMotorSpeeds(int leftSpeed, int rightSpeed);
