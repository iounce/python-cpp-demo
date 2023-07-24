#ifndef __RECT_H
#define __RECT_H

class Rect
{
public:
    Rect();
    Rect(int w, int h);
    ~Rect();
public:
    int width();
    int height();
private:
    int w;
    int h;
};

#endif