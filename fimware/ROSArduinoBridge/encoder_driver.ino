/* *************************************************************
   Encoder definitions for Arduino Nano (ATmega328P)
   
   Using PCINT (Pin Change Interrupts) for high efficiency.
   ************************************************************ */
   
#ifdef USE_BASE

#ifdef ARDUINO_ENC_COUNTER
  volatile long left_enc_pos = 0L;
  volatile long right_enc_pos = 0L;
  static const int8_t ENC_STATES [] = {0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0};  //encoder lookup table
  
  /* Interrupt routine for LEFT encoder (Pins 2 & 3) */
  ISR (PCINT2_vect){
    static uint8_t enc_last=0;
    enc_last <<= 2;
    enc_last |= (PIND & (3 << 2)) >> 2; // Read PD2 and PD3
    left_enc_pos += ENC_STATES[(enc_last & 0x0f)];
  }
  
  /* Interrupt routine for RIGHT encoder (Pins A4 & A5) */
  ISR (PCINT1_vect){
    static uint8_t enc_last=0;
    enc_last <<= 2;
    enc_last |= (PINC & (3 << 4)) >> 4; // Read PC4 and PC5
    right_enc_pos += ENC_STATES[(enc_last & 0x0f)];
  }
  
  void initEncoders() {
    // Port D (Pins 2, 3) configuration
    DDRD &= ~(1 << 2);
    DDRD &= ~(1 << 3);
    PORTD |= (1 << 2); // Pull-up
    PORTD |= (1 << 3); // Pull-up
    PCMSK2 |= (1 << 2) | (1 << 3); // Enable interrupts for PD2, PD3
    
    // Port C (Pins A4, A5) configuration
    DDRC &= ~(1 << 4);
    DDRC &= ~(1 << 5);
    PORTC |= (1 << 4); // Pull-up
    PORTC |= (1 << 5); // Pull-up
    PCMSK1 |= (1 << 4) | (1 << 5); // Enable interrupts for PC4, PC5
    
    // Global interrupt enable for PCINT1 and PCINT2
    PCICR |= (1 << 1) | (1 << 2); 
  }

  long readEncoder(int i) {
    if (i == LEFT) return left_enc_pos;
    else return right_enc_pos;
  }

  void resetEncoder(int i) {
    if (i == LEFT) left_enc_pos = 0L;
    else right_enc_pos = 0L;
  }

#endif

void resetEncoders() {
  resetEncoder(LEFT);
  resetEncoder(RIGHT);
}

#endif
