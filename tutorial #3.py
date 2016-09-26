#========================================#
###         Tutorial No.3              ###
###           PHYS 236                 ###
#========================================#
'''
Content:
1. List
2. Array
3. Define Function.
4. Data Analysis Basic (Board Presentation)
'''
####1. List
##x=[1,2,3,4,5]
##print x+[1] #list append
##
##x=[1,2,3,4,5]
##print x.append(1) #action, not a list
##print x
##
##x=[1,2,3,4,5]
##print x.pop() #FIFO: first in first out
##print x
##
##x=[1,2,3,4,5]
##print x.pop(0)#FILO: first in last out
##print x
##
##x=[1,2,3,4,5]
##print sum(x)
##print min(x)
##
##x=[1,2,3,4,5]
##print x[0]
##print x[-1]
##print x[:]
##print x[2:4]

##2. Array
from numpy import *

##x = array([1,2,3])
##print x
##
##lst = [1,2,3,4,5]
##x = array(lst)
##print x

##x = array([1,2,3,4,5])
##print x+1
##print x[0]

##x =zeros(3)
##print x
##x = zeros([3,2])
##print x

##x = array([1,2,3,4,5])
##print x.sum()
##x = array([[1,10],[2,20],[3,30],[4,40]])
##print x.sum(axis=0)
##print x.sum(axis=1)

##x = array([2,13,4,5])
##print x.sort()
##print x

##3. Function
##def sort(array):
##    less = []
##    equal = []
##    greater = []
##
##    if len(array) > 1:
##        pivot = array[0]
##        for x in array:
##            if x < pivot:
##                less.append(x)
##            if x == pivot:
##                equal.append(x)
##            if x > pivot:
##                greater.append(x)
##        return sort(less)+equal+sort(greater)  
##    else:  
##        return array
####(copyright: Brionius, Stackoverflow)
##print sort(array=[12,4,5,6,7,3,1,15])
