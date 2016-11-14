######################
## Phys-236 Tut     ##
##                  ##
## Guiyang Han      ##
## Nov. 14. 2016    ##
######################
## Romberg Integration
from numpy import *
# Define the function(some function that you are ask to do)
def afun(t):
    return exp(t)

# Lets say we want to integrate this from 0.3 to 1.7
low_b = 0.3
up_b = 1.7

# Trapezoid Rule
def trapz(n): # n is how many 'trapezoid' with in the estimation
    timestep = (up_b - low_b)/n
    sum_so_far = afun(low_b)+afun(up_b)   # initial value
    for tracker in range(1,n): # sum internal values as summation.
        sum_so_far += 2.0*afun(low_b + tracker*timestep)
    return 0.5*timestep*sum_so_far
        
#Romberg's method:
#I will not define a general case here, because that will be too
#similar to assignment.(you should do it)

# hint:
# def Rombe(layer_num): 
#   first_layer = ...# you should have all your values
#   current_layer = []
#   for current_num in range(1, layer_num+1):
#

## Now, I do an example just to illustrate how Romberg works:
T_11 = trapz(1)
T_12 = trapz(2)
T_13 = trapz(4)
T_14 = trapz(8)

T_21 = T_12+(T_12-T_11)/3
T_22 = T_13+(T_13-T_12)/3
T_23 = T_14+(T_14-T_13)/3

T_31 = T_22+(T_22-T_21)/15
T_32 = T_23+(T_23-T_22)/15

print T_32
