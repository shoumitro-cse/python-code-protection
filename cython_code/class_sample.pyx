
cdef class B(object):

    def       d(self): return 20
    cpdef public int c(self): return 30
    cpdef public int p(self): return 40

    cpdef public int hello(self):
        print("Hello world")
        return 500

    cdef  int ab,bc,cc
    #B.ab=600
    #B.bc=900
    cpdef public int sum2(self):
        self.ab=600
        self.bc=900
        self.cc=self.ab+self.bc
        return self.cc

    cdef int a,b,s
    cpdef int sum(self,a,b):
        self.a=a
        self.b=b
        self.s=self.a+self.b
        return self.s

    cpdef int get_sum(self,a,b):
        return self.sum(a,b)
