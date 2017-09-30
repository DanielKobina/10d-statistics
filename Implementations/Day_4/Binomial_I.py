"""
Objective:
In this challenge, we learn about binomial distributions. 
  Check out the Tutorial tab for learning materials!

Task:
The ratio of boys to girls for babies born in Russia is 1.09 to 1. If there is 1 child born per birth, 
  what proportion of Russian families with exactly 6 children will have at 3 least boys?

Write a program to compute the answer using the above parameters. 
  Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

Input Format:
A single line containing the following values:
  1.09  1
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

b,g = input().split() #Number of boys and girls respectively
b = float(b)
g = float(g)

p = b/(b+g) #Probabiliyt of child being a boy
x = 3 #Number of children to be boys for this problem
n = 6 #Total number of children

tot = 0
for i in range(x,n+1): #Cumulative Distribution function
    tot += binomial(i,n,p) #Iteratively call Mass Distribution function
    
output = "{:.3f}".format(tot)
print(output)
