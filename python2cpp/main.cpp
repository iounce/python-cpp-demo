#include<iostream>
#include "rect.h"

using namespace std;

void main()
{
    Rect r = Rect(11, 22);
    cout << r.width() << "," << r.height() << endl;
}