"""
Objective:
In this challenge, we learn about Poisson distributions. 
  Check out the Tutorial tab for learning materials!

Task:
A random variable, X, follows Poisson distribution with mean of 2.5. 
  Find the probability with which the random variable X is equal to 5.

Input Format:
The first line contains X's mean. The second line contains the value we want the probability for:
  2.5
  5
"""

import math

def factorial(val):
    """Factorial equation -> val!
    Input: value (Integer value)
    Output: Factorial of given value"""
    
    if val <= 1: #Factorial of 0 and 1 equal 1, negative values not considered in problem
        return 1
      
    ret = val * factorial(val-1) #Recursive call
    return ret

def poisson(u,x):
    """Poisson Mass Distribution function:
    equation:   [e ^ -u] * [u ^ x] / x!
    
    Input: u (mean of poisson distribution)
           x (trials of interest)
    Output: probability of function"""
    
    top = (math.exp(-u)) * (u**x)
    bot = factorial(x)
    
    return top/bot
    
u = float(input())
x = int(input())

output = poisson(u,x)
print("{:.3f}".format(output))
