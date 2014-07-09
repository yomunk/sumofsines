#include "sumofsines.h"

int step = 13;
int direction = 12;
int i=0;
float time = 0;

void setup() {
  pinMode(step, OUTPUT);
  pinMode(direction, OUTPUT);
  digitalWrite(step, HIGH);
}

void loop() {
  time = millis()/1000;
  if (step_time[i]<time) {
    digitalWrite(direction, step_direction[i]);
    digitalWrite(step, LOW);
    delayMicroseconds(5);
    digitalWrite(step, HIGH);
    i++;
  }
}

