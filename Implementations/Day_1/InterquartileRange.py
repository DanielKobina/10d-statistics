"""
Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, , of integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of decimal place (i.e., format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in arrays and .
The second line contains space-separated integers describing the respective elements of array .
The third line contains space-separated integers describing the respective elements of array .
"""

def medianF(N,A):
    '''
    finds median of array
    input: N,number of elements in array
           A, array of integers
    return: median of array
    '''
    if N%2 == 0: #even
        h1 = int(N/2)-1
        h2 = int(N/2)
        
        v1 = A[h1]
        v2 = A[h2]
        
        mid = (v1+v2)/2
        return mid
    
    else: #odd
        halfN = int(N/2)
        mid = A[halfN]
        return mid

N = int(input())
A = input().split() #create array from string
F = input().split()

A = [int(item) for item in A] #change value and frequency to integers
F = [int(item) for item in F]

L = [] #list with values appearing in correspondence to their frequencies
count = 0 #number of elements in list L

for i in range(N):
    for j in range(F[i]): #append to list the number of times value appears as frequency
        L.append(A[i])
        count += 1

OrdL = sorted(L)
halfN = int(count/2)

if N%2 == 0: #even
    low = OrdL[:halfN]
    high = OrdL[halfN:]
    
else: #odd
    halfN += 1
    
    low = OrdL[:halfN]
    high = OrdL[halfN+1:]

Q3 = medianF(halfN,low)
Q1 = medianF(halfN,high)

print("{:.1f}".format(float(Q1-Q3)))
    
