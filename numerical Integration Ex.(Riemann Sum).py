############ Riemann Sum Example#############
# Riemann sum use middle points to construct
# suitable rectangles to estimate integrations.
# Refers to lecture 9 Slide 10.


## Q: find  the estimation to:
# integral f(x) from 2 to 4.5
#    where f(x) = 2*x/(1+e^x)

from numpy import *
## find x and y:
delta_x = (3.5-2)/100 # lets say we want 100 pieces
x_list = linspace(2,3.5-delta_x,100) # define values that we want to intake, and in total, we pick 100 of them
# we use 3.5-0.015 instead of 3.5 is because we want to exclude the last point.
# if we use the left point to estimate the interval, we dont want the last point.

## define the function to compute y for each element in list of x.
def f(x):
    return 2*x/(1+e**x)

## compute all y values for list of x.
y_list = f(x_list) # when we call like this, the function is acting on seperate elements in x list.


##now, if we plot here  we will see that, we are exactly plot the function f(x)
import matplotlib.pyplot as plt
plt.plot(x_list,y_list)
plt.show()
# the plot is not necessary, and the complicated x term is just spicifying
#   the x-axis.

## now, find the area:
area_piece_list = y_list * delta_x  # for each point y, find its corresponding area.
integration_value = area_piece_list.sum() # summing over all the y slices.
print integration_value
print 'Note that array and sum in array are useful commands. There is hardly a list equivalence version'
