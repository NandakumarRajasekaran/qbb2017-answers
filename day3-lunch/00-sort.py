#!/usr/bin/env python

import random
r = random.randint(1,100)
#print r


nums=range(10)
#print nums
# nums

key=7

"""for i in xrange(len(nums)):
    v=nums[i]
    #print "the %dth number is %d" %(i,v)
    if (v==key):
        print "found at position %d" %(i)
"""
"""
temp=nums
flag=False
idx=0
print temp
mid=len(temp)/2
print mid
val=temp[mid-1]
print val
val1=temp[mid]
idx+=mid
while flag==False:
  #  temp=nums
    print temp
    
    print mid
    
    print val
    
    
    print idx
    if key==val:
        idx+=mid
        flag=True
        print "Done!"
        print idx 
    elif key>val:
        temp=temp[mid:]
        mid=(len(temp)/2)
        idx+=mid
        val=temp[mid-1]
    else:
        temp=temp[0:mid]
        mid=(len(temp)/2)
        idx-=mid
        val=temp[mid-1]
 
"""    
lo=0
hi=len(nums) 
print nums
#binary search
while lo<hi:
    mididx=(lo+hi)/2
    mid=nums[mididx]
    
    if (mid==key):
        print "Found it at %d" % (mididx)
        break
    elif key>mid:
        lo=mididx+1
    else:
        hi=mididx
    
         
          
        
    
    