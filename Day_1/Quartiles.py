"""
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains space-separated integers describing the array's elements.
"""

def median_finder(A,N):

    if N%2 == 0: #even
        halfN = int(N/2)
        
        h1 = A[halfN-1] #Python uses 0 indexing
        h2 = A[halfN]
        mid = (h1+h2)/2

    else: #odd
        halfN = int(N/2)
        mid = A[halfN]
    
    return mid

N = int(input()) #number of elements in array
A = input().split() #array

A = [int(x) for x in A] #integers
A = sorted(A) #sort array

mid = median_finder(A,N) #Q2, after finding mid, split up array into upper and lower

upper = [x for x in A if x > mid]
upL = len(upper)

lower = [x for x in A if x < mid]
loL = len(lower)

Q1 = median_finder(upper,upL)
Q2 = mid
Q3 = median_finder(lower,loL)

print(int(Q3))
print(int(Q2))
print(int(Q1))
