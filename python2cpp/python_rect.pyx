# distutils: language = c++

from python_rect cimport Rect

cdef class PyRect:
    cdef Rect rect

    def __init__(self, w, h):
        self.rect = Rect(w, h)

    def get_width(self):
        return self.rect.width()

    def get_height(self):
        return self.rect.height()