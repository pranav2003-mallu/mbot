/* *************************************************************
   Encoder driver function definitions for Arduino Nano
   ************************************************************ */
   
#ifdef ARDUINO_ENC_COUNTER
  #define LEFT_ENC_PIN_A 2
  #define LEFT_ENC_PIN_B 3
  #define RIGHT_ENC_PIN_A A4
  #define RIGHT_ENC_PIN_B A5
#endif
   
void initEncoders();
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();
