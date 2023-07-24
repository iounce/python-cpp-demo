cdef extern from "rect.h":
    cdef cppclass Rect:
        Rect() except +
        Rect(int w, int h) except +
        int width()
        int height()