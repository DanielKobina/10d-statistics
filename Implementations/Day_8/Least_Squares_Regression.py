"""
Objective
In this challenge, we practice using linear regression techniques. 
  Check out the Tutorial tab for learning materials!

Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
  Each student's Math aptitude test score, x, and Statistics course grade, y, 
  can be expressed as the following list of (x,y) points:
  
  (95,85)
  (85,95)
  (80,70)
  (70,65)
  (60,70)

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? 
  Determine the equation of the best-fit line using the least squares method, 
  then compute and print the value of y when x = 80.

Input Format:
There are five lines of input; each line contains two space-separated integers describing a student's respective x and y grades:
  95 85
  85 95
  80 70
  70 65
  60 70
"""

def intercept(x,y,n,b):
    """Intercept
    equation: mean(y) - slope * mean(x)
    Input: x (x array)
           y (y array)
           n (number of elements in each array)
           b (slope between x and y)
    Output: Intercept between independent variable (x) and dependent variable (y)"""
    uy = sum(y)/n
    ux = sum(x)/n
    
    return uy - b * ux

def slope(x,y,n):
    """Slope
    equation: Pearson_CC * std(y)/std(x)
    Input: x (x array)
           y (y array)
           n (number of elements in each array)
    Output: Slope between indepedent variable (x) and dependent variable (y)"""
    
    nxy = 0
    nx = 0
    ny = 0
    nx2 = 0
    
    for i in range(n):
        nxy += x[i]*y[i]
        nx += x[i]
        ny += y[i]
        nx2 += x[i] * x[i]
        
    top = n * nxy - nx * ny
    bot = n * nx2 - nx**2
    
    return top/bot

x = []
y = []
for i in range(5):
    vals = input().split()
    x.append(int(vals[0]))
    y.append(int(vals[1]))
    
n = len(x)
b = slope(x,y,n)
a = intercept(x,y,n,b)

final = 80 * b + a
print("{:.3f}".format(final))
