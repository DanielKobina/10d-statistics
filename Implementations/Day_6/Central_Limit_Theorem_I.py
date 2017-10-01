"""
Objective:
In this challenge, we practice solving problems based on the Central Limit Theorem. 
  Check out the Tutorial tab for learning materials!

Task:
A large elevator can transport a maximum of pounds. 
  Suppose a load of cargo containing boxes must be transported via the elevator. 
  The box weight of this type of cargo follows a distribution with a mean of pounds and 
  a standard deviation of pounds. Based on this information, what is the probability that 
  all boxes can be safely loaded into the freight elevator and transported?

Input Format:
There are lines of input (shown below):
  9800
  49
  205
  15

The first line contains the maximum weight the elevator can transport. 
  The second line contains the number of boxes in the cargo. 
  The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.
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
        u = int(line)

    else:
        std = int(line)

uT = n * u #Sample mean of the distribution
stdT = n**(1/2) * std #Sample standard deviation of the distribution

output = normal_cdf(uT,stdT,limit)
print("{:.4}".format(output))
