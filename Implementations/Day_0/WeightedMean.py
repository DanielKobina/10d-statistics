"""
Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers and an array, , representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of decimal place (i.e., format).

Input Format
The first line contains an integer, , denoting the number of elements in arrays and .
The second line contains space-separated integers describing the respective elements of array .
The third line contains space-separated integers describing the respective elements of array .
"""

N = int(input())
X = input().split()
W = input().split()

X = [int(c) for c in X] #change from strings to integers
W = [int(c) for c in W]

top = 0
bot = 0

for i in range(N): #weighted mean formula
    top += X[i] * W[i] 
    bot += W[i]
   
#print(float(int(top/bot)))
print("{:.1f}".format(top/bot)) #1 decimal point
