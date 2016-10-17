##################################
'''
Assignment 3 Answer Sketch

Guiyang Han
'''
##################################

## Q5a:
from math import erfc, sqrt

# we compute the joint probability
prob_getA = erfc(2.8/sqrt(2)) # the equation to compute probabilty of event A
prob_getB = erfc(4.1/sqrt(2)) # similar for event B

prob_joint = prob_getA*prob_getB # since two events are independent,
                                 #  we simply mutiply them to find happen togeth
print 'joint probability is', prob_joint
# We reverse the equation to find significance

#(method 1: use loop to find the significance)
error = 0.0001  # allow systme to have some error
test_joint = 2.0*error + prob_joint # initial a value.
sigma_joint = 0.0
while abs(test_joint - prob_joint) > error:
    test_joint = erfc(sigma_joint/sqrt(2.0))
    sigma_joint += 0.001

print 'Joint Significance is', sigma_joint

#(method 2: directly use inverse function)
from scipy.special import erfcinv

sigma_joint = erfcinv(prob_joint)*sqrt(2)
print 'Joint Significance is', sigma_joint
    
## Q5b:
from math import erfc, sqrt

# find the prob of getting a single event 
prob_get1 = erfc(3.5/sqrt(2))

# given 3.5 is the highest significance, all others are lower than 3.5,
# which means have higher probability of happening.

# an upper bound would be all others have sigma = 0 (definitely happen)
upper_bound = prob_get1 * (erfc(0) ** 7) * 8 # *8 because there are 8 experiments
                                             # and each of them could be 3.5 significance

# an lower bound would be all others have sigma = 3.5
lower_bound = prob_get1 ** 8 * 1 # there is only 1 case where all sigma =3.5

# then juse the function in Q5a to compute the sigma.
sigma_upper_bound = erfcinv(upper_bound)*sqrt(2)
sigma_lower_bound = erfcinv(lower_bound)*sqrt(2)
print '8 experiments have most', sigma_upper_bound, '*sigma total significance','have least',sigma_lower_bound,'*sigma total significance'


## Q6a:
from numpy import loadtxt # use this to import

data = loadtxt('testdata_short.txt')
data = [float(x) for x in data] # insure that everything in data is float number.

# find mean and variance:
mean = sum(data)/len(data)

variance = 0
for x in data:
    variance += (x-mean) ** 2
variance = variance /len(data)

print 'the mean and variances are',mean,variance

# plot and show the data:
from pylab import hist, savefig

hist(data)
savefig('figure.png')

##Q6b,c,d:
# Refer to Q6 a for calcualting things,
#  the following is how you construct the data:

# first use the old data:
data = loadtxt('testdata_short.txt')
data = [float(x) for x in data] 

# now lets say we are in Q6c case,
triple_data = [] # initial an empty list
for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if i==j==k:
                continue
            triple_data.append((data[i]+data[j]+data[k])/3.0)
# now you should have a good data to calculate mode and variance and graph.


## Q6e:
# (from student answer, use without authorize.
#   will be removed anytime.)

from numpy import arange, loadtxt
from pylab import hist, savefig
from matplotlib.pyplot import plot, show, ylabel, xlabel, title
dataset = loadtxt("testdata_short.txt")
#using values from previous trials
varOG=237.819262782 #variance from original distribution
var2=112.506772268 #variance from averaging every pair of 2
var3=72.1180576206 #variance from averaging every pair of 3
var4=52.2954785462 #variance from averaging every pair of 4
plot(1.0,varOG,"bo")
plot(2.0,var2,"bo")
plot(3.0,var3,"bo")
plot(4.0,var4,"bo")
#plotting theory
def theoryvariance(x):
    t= varOG/x
    return t

x = arange(1,5,0.1)
y = theoryvariance(x)
title("Variance vs Pairs Averaged")
ylabel("Variance")
xlabel("Pairs Averaged")
plot(x,y,"r")
savefig('figure.png')

print "yes, the points, outlined in blue, follow the expected behavior, outlined in red, of cental limit theory"
