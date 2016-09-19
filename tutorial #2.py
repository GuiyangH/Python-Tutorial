#========================================#
###         Tutorial No.2              ###
###           PHYS 236                 ###
#========================================#
'''
A great learning Source:  http://www.tutorialspoint.com/python
Content:
1. Variables Assign
2. Packages
3. Input and Output
4. Check and Convert
5. Flow Control
'''


# Part 1: Variable Assign

##a = 1
##b = a
##a = 2
##print b
##a = [1,2]
##b = a
##a = [2,3]
##print b


##a = [1,2]
##b = a
##a[0] = 3
##print 'value of a is ' ,a
##print 'value of b is ' ,b




# Part 2: Packages
# C:\Python27\Lib\site-packages\numpy\polynomial


##from numpy import *
##pi
##inf
##exp(2)
##import numpy as np


# Part 3: input/ output


##h_raw = raw_input('type any letter here for h_raw: ')
##h = input('type any letter here for h: ')
##print 'this is h_raw', h_raw
##print 'this is h',h


##h = input('type any number here for h: ')
##h_raw = input('type any number here for h_raw: ')
##print 'this is h_raw', h_raw
##print 'this is h',h


##h = 7
##print "what's the number 9 afraid of? Answer:",7,'.'
##print "what's the number 9 afraid of? Answer: {}.".format(h)
##print "what's the number 9 afraid of? Answer: %d."%(h)
##print 'Im the first line. \nHe is right.'

# Part 4: Check/ Convert


##h = input('lets try to input something, what is your name?')
##try:
##    float(h)
##    print 'Cant believe your name is a number'
##except ValueError:
##    print h,'is an awesome name!'


##isinstance(3,float)
##isinstance(3.0,float)
##isinstance(3.0,int)


##int('3.2')
##float('3.2')
##str(3.2)


# Part 5: Recurssion

########======= for loop ============######


##for younameit in [1,2,3,4,5]:
##    print younameit


##afunnylist = [[1,2],[2,3],[3,4],[4,5]]
##result = [x[0]+x[1] for x in afunnylist]
##print result

##alist = [[[1],[2]],[[1],[2]],[[1],[2]],
##         [[1],[2]],[[1],[2]],[[1],[2]],
##         [[1],[2]],[[1],[2]],[[1],[2]]]
##for i in alist:
##    for j in i:
##        for k in j:
##            print k
##newlylist = [[[k*2 for k in j] for j in i] for i in alist]
##print newlylist




#########======while loop =============#####



##h = 2
##while h>1:
##    print h

##h = 1
##while h>0:
##    h += 1
##    print 'This is the',h,'times run.'

##h = 1
##while h>0:
##    h += 1
##    print 'I am still run like crazy'
##if h == 2:
##    print 'I stopped'


##h = 1
##while h>0:
##    h += 1
##    print 'Catch me if you can'
##    if h == 3:
##        print 'I just got my head down'
##        print 'And Im a little bit scared tonight \nI need to run just far enough'
##        break




##=========if, break, continue=================##




##h = 1
##if h == 1:
##    print 'h equal to one.'
##if h != 1:
##    print 'h not equal to one.'




##h = 1
##while h >1:
##    h += 1
##    print h
##    break



##for letter in 'alongsentencewithnospaceandrealmeanings':     
##   if letter == 'e':
##      continue
##   print 'Current Letter :', letter

