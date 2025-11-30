#include <stdio.h>

int main() {
  int myInt = 3;
  char myChar = 'F';
  float myFloat = 37.6;
  double myDouble = 127.255;


  printf("%d\t\t", myInt);
  printf("%lu\n", sizeof(myInt));

  printf("%c\t\t", myChar);
  printf("%lu\n", sizeof(myChar));

  printf("%f\t", myFloat);
  printf("%lu\n", sizeof(myFloat));

  printf("%lf\t", myDouble);
  printf("%lu\n", sizeof(myDouble));

  return 0;
}
