#!/usr/bin/env python

print "Basic types .."

a_string= "This is a string"

an_integer=7
i_as_s= str(an_integer)
s_as_r=float("5.689")
a_real =  5.689
truthy=True
falsy=False

"""for value in a_string, a_real, truthy:
    print value, type(value)
"""    
a_list=[1,2,3,4,5]
a_tuple=(1,"foo",3.2)

print a_list, type(a_list)
print a_tuple, type(a_tuple)

#lists are mutable while tuples are not

#lists are referenced and other advanced types like dictionary , etc..
another_list=a_list
another_List[3]=888
print a_list

another_list=list(a_list)