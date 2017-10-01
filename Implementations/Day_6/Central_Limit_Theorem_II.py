"""
Objective:
In this challenge, we practice solving problems based on the Central Limit Theorem. 
  We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

Task:
The number of tickets purchased by each student for the University X vs. 
  University Y football game follows a distribution that has a mean of and a standard deviation of .

A few hours before the game starts, eager students line up to purchase last-minute tickets. 
If there are only tickets left, what is the probability that all students will be able to purchase tickets?

Input Format:
There are lines of input (shown below):

  250
  100
  2.4
  2.0

The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.
"""

import sys
from math import erf

def normal_cdf(u,std,x):
    """Normal Cumulative Distribution function
    equation:   normal_cdf(x) = 0.5 * (1 + erf[(x-u)/std*sqrt(2)])
                where erf(z) = 2/sqrt(pi) * integral from 0 to z of e^(-z^2) * dx
                
    Input: u (mean)
           std (standard deviation) 
           x (value of interest)
    Output: probability of function"""
    
    topz = (x-u)
    botz = (std * 2**(1/2))
    z = topz/botz
    
    return (1 + erf(z))*.5

for idx,line in enumerate(sys.stdin):
    if idx == 0:
        limit = int(line)
        
    elif idx == 1:
        n = int(line)
        
    elif idx == 2:
        u = float(line)

    else:
        std = float(line)

uT = n * u #Sample mean of the distribution
stdT = n**(1/2) * std #Sample standard deviation of the distribution

ans = normal_cdf(uT,stdT,limit)
print("{:.4}".format(ans))
