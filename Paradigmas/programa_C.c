//Programa C
#include <stdio.h>

int x=0,y=0,z=0;

int f(int *x, int y)
{
*x=1;
y=1;
return *x+y;
}

int main(void) {
printf("%d %d %d\n",x,y,z);
z = f(&x,y); 
printf("%d %d %d\n",x,y,z);
return 0;
}
