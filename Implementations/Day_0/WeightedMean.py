"""
Objective:
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean.
    Check out the Tutorial tab for learning materials and an instructional video!

Task:
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
    calculate and print the weighted mean of X's elements. 
    Your answer should be rounded to a scale of decimal place (i.e., 12.3 format).

Input Format:
The first line contains an integer, N, denoting the number of elements in arrays X and W.
    The second line contains N space-separated integers describing the respective elements of array X.
    The third line contains N space-separated integers describing the respective elements of array W.
"""

N = int(input())
X = input().split()
W = input().split()

X = [int(c) for c in X] #Change from strings to integers
W = [int(c) for c in W]

top = 0
bot = 0

for i in range(N): #Weighted mean formula: (X * W) / W
    top += X[i] * W[i] 
    bot += W[i]
   
print("{:.1f}".format(top/bot)) #1 decimal point
