cpdef int test_py(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += x
    print("Y value: ", y)
    return y