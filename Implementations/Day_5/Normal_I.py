"""
Objective:
In this challenge, we learn about normal distributions. 
  Check out the Tutorial tab for learning materials!

Task:
In a certain plant, the time taken to assemble a car is a random variable, X, 
  having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
  What is the probability that a car can be assembled at this plant in:

    1) Less than 19.5 hours?
    2) Between 20 and 22 hours?

Input Format:
There are 3 lines of input (shown below):
  20 2
  19.5
  20 22
"""

from math import pi, erf

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

u, std = input().split() #mean, standard deviation
q1 = float(input()) #question 1 value
q2a,q2b = input().split() #question 2 values

u, std, q2a, q2b = int(u), int(std), int(q2a), int(q2b)

Q1 = normal_cdf(u,std,q1)
print("{:.3f}".format(Q1))

Q2 = normal_cdf(u,std,q2b) - normal_cdf(u,std,q2a)
print("{:.3f}".format(Q2))
