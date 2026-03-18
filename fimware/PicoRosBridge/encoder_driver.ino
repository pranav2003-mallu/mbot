#ifdef USE_BASE

volatile long l_enc_pos = 0L;
volatile long r_enc_pos = 0L;

// Full quadrature state machine for 4x decoding and direction accuracy
static const int8_t Q_STATES[] = {0, -1, 1, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 1, -1, 0};
static uint8_t l_last = 0;
static uint8_t r_last = 0;

void leftEncoderISR() {
  l_last = (l_last << 2) & 0x0F;
  l_last |= (digitalRead(LEFT_ENC_PIN_A) << 1) | digitalRead(LEFT_ENC_PIN_B);
  l_enc_pos += Q_STATES[l_last];
}

void rightEncoderISR() {
  r_last = (r_last << 2) & 0x0F;
  r_last |= (digitalRead(RIGHT_ENC_PIN_A) << 1) | digitalRead(RIGHT_ENC_PIN_B);
  r_enc_pos += Q_STATES[r_last];
}

void initEncoders() {
  pinMode(LEFT_ENC_PIN_A, INPUT_PULLUP);
  pinMode(LEFT_ENC_PIN_B, INPUT_PULLUP);
  pinMode(RIGHT_ENC_PIN_A, INPUT_PULLUP);
  pinMode(RIGHT_ENC_PIN_B, INPUT_PULLUP);
  
  attachInterrupt(digitalPinToInterrupt(LEFT_ENC_PIN_A), leftEncoderISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(LEFT_ENC_PIN_B), leftEncoderISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(RIGHT_ENC_PIN_A), rightEncoderISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(RIGHT_ENC_PIN_B), rightEncoderISR, CHANGE);
}

long readEncoder(int i) {
  if (i == LEFT) return l_enc_pos;
  else return r_enc_pos;
}

void resetEncoder(int i) {
  if (i == LEFT) l_enc_pos = 0L;
  else r_enc_pos = 0L;
}

void resetEncoders() {
  resetEncoder(LEFT);
  resetEncoder(RIGHT);
}

#endif
