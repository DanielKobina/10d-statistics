"""
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average,12% of the pistons they manufacture are rejected because they are incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:
    No more than 2 rejects?
    At least 2 rejects?

Input Format

A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):
  12  10
"""


def factorial(val):
    """factorial equation
    input: value
    output: factorial of value
    
    equation    val!"""
    
    if val <= 1:
        return 1
    ret = val * factorial(val-1)
    return ret

def combination(n,x): 
    """combination equation
    input: values n and r
    output: combination of n and r
    
    equation        n!
                  r!(n-1!)"""
    
    top = factorial(n)
    bot = factorial(x) * factorial(n-x)
    return top/bot

def binomial(x,n,p):
    """binomial mass distribution function
    input: values x(number of successfull trials) n(number of trials), p(probability of successfull trial)
    output: probability of function
    
    equation  (n;x) * (p**x) * (q**(n-x))"""

    return (combination(n,x)) * (p**x) * ((1-p)**(n-x))

p = .12 #probability a manufactured piston is rejected
x = 2 #aimed number of pistons
n = 10 #total batch of pistons

one = 0
for i in range(0,x+1): #Cumulative Distribution function
    one += binomial(i,n,p) #probability mass function
    
two = 0
for i in range(x,n+1): #Cumulative Distribution function
    two += binomial(i,n,p) #probability mass function
    
one = "{:.3f}".format(one)
print(one) 

two = "{:.3f}".format(two)
print(two) 
