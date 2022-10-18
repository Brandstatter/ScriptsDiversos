//Programa D - Atnção: Linguagem C++
#include <iostream>
using namespace std;

int f(int &batatinha, int &y)
{
	batatinha=1;
	y=1;
	return x+y;
}

int main() {
    int x=0,y=0,z=0;
    cout << x << y << z << endl;
    z = f(x,y);
    cout << x << y << z << endl;
    return 0;
}
