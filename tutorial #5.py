##############################
#       Tutorial #5          #
#                            #
##############################
from numpy import *
from math import erf, factorial
from matplotlib.pyplot import plot, show
## Content:
# 1. Gaussian Distribution

## 1. Gaussian

# define the function:
def gaussian(x, mu, sig):
    return 1/(sqrt(2*pi)*sig)*exp(-power(x - mu, 2.0) / (2.0 * power(sig, 2.0)) )

# Show a sample graph
mu = 50
sig = 10.0
x = linspace(0, 100, 100)
y = gaussian(x,mu,sig)
plot(x,y)
show()

# find the probability within a range of x:
print erf(2)  #The prob of getting datas within 2sigma
print erf(2)-erf(1) # the prob og getting datas with [1sigma, 2sigma]

## Binomial & Poisson:
# factorial:
print factorial(4)
def binomial(p, n, k):
    return factorial(n)/factorial(k)/factorial(n-k)*power(p,k)*power(1-p,n-k)
#
# Visualize the Data
p = 0.7
n = 35
k = range(0,30)
y = []
for a in range(0,30):
    y = y + [binomial(p,n,a)]
plot(k,y)
show()

# Possion Distribution
import webbrowser
webbrowser.open('Poisson_pmf.jpg')
