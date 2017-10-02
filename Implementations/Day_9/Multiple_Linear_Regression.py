"""
Objective:
In this challenge, we practice using multiple linear regression. 
  Check out the Tutorial tab for learning materials!

Task:
Andrea has a simple equation: Y = a + b1 * f1 + b2 * f2 +......+ bm * fm
  for (m+1) real constants (a, f1, f2,..., fm). We can say that the value of Y depends on m features. 
  Andrea studies this equation for n different feature sets (f1,f2,f3,...fm) and records each respective value of Y. 
  If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

Note: You are not expected to account for bias and variance trade-offs.

Input Format:
The first line contains 2 space-separated integers, m (the number of observed features) and 
  n (the number of feature sets Andrea studied), respectively.
  Each of the n subsequent lines contain m+1 space-separated decimals; the first m elements are features (f1,f2,f3,...fm), 
  and the last element is the value of Y for the line's feature set.
  The next line contains a single integer, q, denoting the number of feature sets Andrea wants to query for.
  Each of the q subsequent lines contains m space-separated decimals describing the feature sets.
"""

import numpy as np
from numpy.linalg import inv

def find_coefficients(X,Y):
    """Determine coefficients (B) from equation: Y = X * B
    Input: X (matrix of features for each sample)
           Y (vector of clasifiers)
    Output: Weight vector"""
    b1 = inv(np.dot(X.T,X)) #(Xt * X) ^ -1
    b2 = np.dot(X.T,Y)# Xt * Y
    
    return np.dot(b1,b2)

m,n = input().split()
m,n = int(m),int(n) #Number of: features and trials respectively

X,Y,P = [],[],[] #List of: feature vectors, values, derived weights respectively
for i in range (n):
    arr_L = input().split()
    arr_L = [float(c) for c in arr_L]
    #arr_L in the form [x1, x2, x3,....xm, y]
    
    x,y = arr_L[:-1],arr_L[-1]
    #Split up x and y
    
    x = [1] + x  
    #Add 1 element to beginning of each x vector
    
    X.append(np.array(x))
    Y.append(y)
    
q = int(input())

for i in range(q):
    p = input().split()
    p = [float(c) for c in p]
    p = [1] + p
    #Add 1 element to beginning of each p vector
    
    P.append(np.array(p))
    
X = np.array(X)
Y = np.array(Y)
B = find_coefficients(X,Y) #Find weights between original features and values
P = np.array(P)
#Using numpy arrays for general efficiency

Final = np.matmul(P,B) #Use weight vectors on current dataset 
for ele in Final:
    print("{:.2f}".format(ele))
