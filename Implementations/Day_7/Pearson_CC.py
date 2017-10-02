"""
Objective:
In this challenge, we practice calculating the Pearson correlation coefficient. 
  Check out the Tutorial tab for learning materials!

Task:
Given two -element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

Input Format:
The first line contains an integer, n, denoting the size of data sets X and Y.
  The second line contains n space-separated real numbers (scaled to at most one decimal place), defining data set X.
  The third line contains n space-separated real numbers (scaled to at most one decimal place), defining data set Y.
"""

def covariance(n,x,y,xu,yu):
    """Covariance
    equation: (x[i] - ux) * (y[i] - uy) for every i from 1 (0) to n (n-1)
    
    Input: n (number of elements)
           x (x array)
           y (y array)
           xu (mean of x array)
           yu (mean of y array)
    Output: Covariance between x and y"""
    
    total = 0
    for i in range(n):
        xpart = x[i] - xu
        ypart = y[i] - yu
        total += xpart * ypart

    return total

def variance(n,arr,u):
    """Variance
    equation: (val[i] - u)^2 for every i from 1 (0) to n (n-1)
    
    Input: n (number of elements)
           arr (array of elements)
           u (mean of array)
    Output: Variance of elements in array"""
    
    total = 0
    for i in range(n):
        total += (arr[i]-u)**2
        
    return total
        
n = int(input()) #Number of elements in both array x and y
x = input().split()
x = [float(i) for i in x] #Array x
y = input().split()
y = [float(i) for i in y] #Array y

xu = sum(x)/len(x) #Mean of array x
yu = sum(y)/len(y) #Mean of array y

Sxy = covariance(n,x,y,xu,yu) #Covariance between x and y
Sxx = variance(n,x,xu) #Variance of x
Syy = variance(n,y,yu) #Vacriance of y

r = Sxy / ((Sxx)**(1/2) * (Syy)**(1/2)) #Pearson Correlation Coefficient
print("{:.3f}".format(r))
