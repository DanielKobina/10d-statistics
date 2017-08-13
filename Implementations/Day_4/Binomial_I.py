"""
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is . If there is child born per birth, what proportion of Russian families with exactly children will have at least boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of decimal places (i.e., format).

Input Format

A single line containing the following values:
  1.09  1
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
    
    equation:        n!
                  r!(n-1!)"""
    
    top = factorial(n)
    bot = factorial(x) * factorial(n-x)
    return top/bot

def binomial(x,n,p):
    """binomial mass distribution function
    input: values x(number of successfull trials) n(number of trials), p(probability of successfull trial)
    output: probability of function
    
    equation:  (n;x) * (p**x) * (q**(n-x))"""

    return (combination(n,x)) * (p**x) * ((1-p)**(n-x))

b,g = input().split()
b = float(b)
g = float(g)

p = b/(b+g)
x = 3 #Number of children that may be boys
n = 6 #Total number of children

tot = 0
for i in range(x,n+1): #Cumulative Distribution function
    tot += binomial(i,n,p) #probability mass function
    
output = "{:.3f}".format(tot)
print(output) #About 5:38.67 minutes to create, About 10:03.72 minutes to redo
