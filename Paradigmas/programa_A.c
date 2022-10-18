//Programa A
#include <stdio.h>

int f(int x, int y)
{
int z;
x=1;
y=1;
z = x+y;
return z;
}

int main(void) {
int x=0,y=0,z=0; //variáveis locais
printf("%d %d %d\n",x,y,z); 
z = f(x,y); 
printf("%d %d %d\n",x,y,z); 
return 0;
}
