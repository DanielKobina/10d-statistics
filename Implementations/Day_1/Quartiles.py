"""
Objective:
In this challenge, we practice calculating quartiles. 
    Check out the Tutorial tab for learning materials and an instructional video!

Task:
Given an array, X, of n integers, calculate the respective first quartile (Q1), 
    second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

Input Format:
The first line contains an integer, n, denoting the number of elements in the array.
    The second line contains n space-separated integers describing the array's elements.
"""

def median_finder(A,N):
    """
    Median of array A
    Input: A (array containing numeric values)
           N (length of the array)
    Output: The median of array A"""
    
    halfN = int(N/2)
    
    if N%2 == 0: #Even array length
        h1 = A[halfN-1] #Python uses 0 indexing
        h2 = A[halfN]
        mid = (h1+h2)/2

    else: #Odd array length
        mid = A[halfN]
    
    return mid

N = int(input()) #Number of elements in array
A = input().split() #Array of elements

A = [int(x) for x in A] #Change array from strings to integers
A = sorted(A) #Sort array

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
