"""
Objective:
In this challenge, we practice solving problems based on the Central Limit Theorem. 
  We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

Task:
You have a sample of 100 values from a population with mean 500 and with standard deviation 80. 
  Compute the interval that covers the middle 95% of the distribution of the sample mean; 
  in other words, compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note that z is the z-score.

Input Format:
There are five lines of input (shown below):
  100
  500
  80
  .95
  1.96

The first line contains the sample size. 
  The second and third lines contain the respective mean (u) and standard deviation (std). 
  The fourth line contains the distribution percentage we want to cover (as a decimal), 
  and the fifth line contains the value of .
"""

import sys
from math import erf

def intervals(n,u,std,z):
    """ Finds the probability that our end value is between -z and z
    equation:   u+- z * std/ sqrt(n)
    
    Input: n (number of trials)
           u (mean)
           std (standard deviation)
           z (z-score)
    Output: probability of equation"""
    part = z * std
    part = part / (n**(1/2))
    
    low = u - part
    high = u + part
    
    return low,high

n = int(input()) #Number of trials
u = int(input()) #Mean
std = int(input()) #Standard deviation
p = float(input()) #Probabiliity
z = float(input()) #Z-score

A,B = intervals(n,u,std,z)
print("{:.2f}".format(A))
print("{:.2f}".format(B))
