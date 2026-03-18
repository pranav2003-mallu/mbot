#ifdef USE_BASE

void initMotorController() {
  pinMode(LEFT_PWM, OUTPUT); 
  pinMode(LEFT_DIR, OUTPUT); 
  pinMode(RIGHT_PWM, OUTPUT); 
  pinMode(RIGHT_DIR, OUTPUT); 
}

void setMotorSpeed(int i, int spd) {
  int pwm = abs(spd);
  // limit max PWM to MAX_PWM for Pico's default 8-bit analogWrite
  if (pwm > MAX_PWM) pwm = MAX_PWM;
  
  if (i == LEFT) {
    if (spd >= 0) {
      digitalWrite(LEFT_DIR, HIGH); // Adjust HIGH/LOW based on actual wiring
    } else {
      digitalWrite(LEFT_DIR, LOW);
    }
    analogWrite(LEFT_PWM, pwm);
  } else {
    // RIGHT
    if (spd >= 0) {
      digitalWrite(RIGHT_DIR, HIGH);
    } else {
      digitalWrite(RIGHT_DIR, LOW);
    }
    analogWrite(RIGHT_PWM, pwm);
  }
}

void setMotorSpeeds(int leftSpeed, int rightSpeed) {
  setMotorSpeed(LEFT, leftSpeed);
  setMotorSpeed(RIGHT, rightSpeed);
}

#endif
