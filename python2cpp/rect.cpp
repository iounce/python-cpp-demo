#include "rect.h"

Rect::Rect()
{
    w = 0;
    h = 0;
}

Rect::Rect(int w, int h)
{
    this->w = w;
    this->h = h;
}

Rect::~Rect()
{
}

int Rect::width()
{
    return w;
}
    
int Rect::height()
{
    return h;
}