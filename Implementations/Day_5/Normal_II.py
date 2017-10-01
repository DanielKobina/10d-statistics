"""
Objective:
In this challenge, we go further with normal distributions. 
  We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task:
The final grades for a Physics exam taken by a large group of students have 
  a mean of u = 70 and a standard deviation of std = 10. 
  If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

    1) Scored higher than 80 (i.e., have a grade > 80)?
    2) Passed the test (i.e., have a grade >= 60)?
    3) Failed the test (i.e., have a grade < 60)?

Find and print the answer to each question on a new line, rounded to a scale of decimal places.

Input Format:
There are 3 lines of input (shown below):
  70 10
  80
  60
"""

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

u, std = input().split() #mean, standard deviation
u,std = int(u),int(std)
v1 = int(input()) #Question 1 value
v23 = int(input()) #Question 2 and 3 value

q1 = 100 * (1 - normal_cdf(u,std,v1))
q2 = 100 * (1 - normal_cdf(u,std,v23))
q3 = 100 * normal_cdf(u,std,v23)

#Calling the normal_cdf function alone indicates: probability(-infinity to value). (i.e. grade <= or < 60)
#Using 1 - normal_cdf indicates: 1 - probability(value to infinity), identical to opposite of value to infinity which becomes similar to above comment. (i.e. 80 >= or > grade)

print("{:.2f}".format(q1))
print("{:.2f}".format(q2))
print("{:.2f}".format(q3))

"""
Tried 68-95-99 rule, but numbers are slightly off from solution
68.27% within 1 standard deviation
95.45% within 2 standard deviations
99.73% within 3 standard deviations

f_t = 13.59 + 2.14
s = 34.135 + 34.135 + 13.59 + 2.14
print("{:.2f}".format(f_t)) about 17.53
print("{:.2f}".format(s)) about 84.00
print("{:.2f}".format(f_t)) about 15.73
"""
