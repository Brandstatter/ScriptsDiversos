//Programa A_trace
#include <stdio.h>

int f(int x, int y)
{
int z;
printf("Endereços (l-values) no RA de f:\n");
printf("%X %X %X\n",&x,&y,&z);
x=1;
y=1;
z = x+y;
printf("Valores (r-values) no RA de f:\n");
printf("%d %d %d\n",x,y,z);
return z;
}
 
int main(void) {
int x=0,y=0,z=0;
printf("Endereços (l-values) no RA da main:\n");
printf("%X %X %X\n",&x,&y,&z);
printf("Valores (r-values) no RA da main:\n");
printf("%d %d %d\n",x,y,z);
z = f(x,y);
printf("Novos valores (r-values) no RA da main após chamar f:\n");
printf("%d %d %d\n",x,y,z);
return 0;
}
