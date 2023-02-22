#Route is a Cython class
cdef class Route:

    # Not available in Python-space:
    #Aavailable in Cython-space:
    cdef  double offset

    # Available in Python-space:
    #Aavailable in Cython-space:
    cdef public double freq

    # Available in Python-space, but only for reading:
    #Aavailable in Cython-space,but only for reading and writing:
    cdef readonly double scale

    # Available in Python-space:
    #Aavailable in Cython-space:
    cdef public :
        int a
        float b
        long c
        double d
    Route().a=90 #not set value

    # Not available in Python-space:
    #Aavailable in Cython-space:
    cdef:
        int aa
        float bb
        long cc
        double dd


    # Not available in Python-space: (cdef method)
    #available in Cython-space:
    cdef public  void fun(self):
        self.a=12
        Route().a=90 #not set value
        print("cython fun calling",self.a)
        #print("cython fun calling",Route().a) #not work


    #Available in Python-space: ( cpdef method )
    #Aavailable in Cython-space:
    cpdef pub(self):
        self.fun()


#Cython-space:
#rc variable use all field and method Route class
cdef Route rc 
rc=Route()
rc.fun()
rc.pub()
rc.a=78
rc.aa=80
rc.freq=89.7
rc.scale=756.0
rc.offset=23.90
print(rc.scale)



#Python-space:
# rp variable only use method(cpdef, def) and  field(public & readonly) 
#Route rp # not work
rp=Route()
#rp.fun()  # Not available
rp.pub()
rp.a=78
#rp.aa=80  # Not available
rp.freq=89.7
#rp.offset=23.90  # Not available
#rp.scale=756.0  # objects is not writable
print(rp.scale)





#not work (it use cppclass )
#cdef Route rc = new Route() 






