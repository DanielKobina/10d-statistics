"""
Objective:
In this challenge, we go further with binomial distributions. 
    We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task:
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture 
    are rejected because they are incorrectly sized. 
    What is the probability that a batch of 10 pistons will contain:
        -No more than 2 rejects?
        -At least 2 rejects?

Input Format:
A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):
  12  10
"""

def factorial(val):
    """Factorial equation -> val!
    Input: value (Integer value)
    Output: Factorial of given value"""
    
    if val <= 1: #Factorial of 0 and 1 equal 1, negative values not considered in problem
        return 1
      
    ret = val * factorial(val-1) #Recursive call
    return ret

def combination(n,x): 
    """Combination equation:
                    n!
                  x!(n-x!)
                  
    Input: n (number of trials)
           r (number of choices)
    Output: Combination of n and x"""
    
    top = factorial(n)
    bot = factorial(x) * factorial(n-x)
    return top/bot

def binomial(x,n,p):
    """Binomial Mass Distribution function
    equation:  (n choose x) * (p ^ x) * (q ^ (n-x))
    
    Input: x (number of successfull trials) 
           n (number of trials)
           p (probability of successfull trial)
    Output: probability of function"""

    return (combination(n,x)) * (p**x) * ((1-p)**(n-x))

p = .12 #Probability a manufactured piston is rejected
x = 2 #Aimed number of pistons
n = 10 #Total number of pistons

one = 0
for i in range(0,x+1): #Cumulative Distribution function
    one += binomial(i,n,p) #Mass Distribution function
    
two = 0
for i in range(x,n+1): #Cumulative Distribution function
    two += binomial(i,n,p) #Mass Distribution function
    
one = "{:.3f}".format(one)
print(one) 

two = "{:.3f}".format(two)
print(two) 
