#include "func.h"
#include "bird.h"

#include <iostream>
using namespace std;

void main()
{
    int a = 1;
    int b = 2;

    Swap<int>(a, b);

    double i = 11.22;
    double j = 12.34;

    Swap<double>(i, j);

    Bird bird("ABC");
    cout << bird.GetName() << endl;
    bird.Fly();
}