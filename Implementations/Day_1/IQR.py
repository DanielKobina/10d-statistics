"""
Objective:
In this challenge, we practice calculating the interquartile range. 
    We recommend you complete the Quartiles challenge before attempting this problem.

Task:
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, 
    construct a data set, S, where each xi occurs at frequency fi. 
    Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

Tip: 
Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, 
    and be sure to not include the median in your upper and lower data sets.

Input Format:
The first line contains an integer, n, denoting the number of elements in arrays X and F.
    The second line contains n space-separated integers describing the respective elements of array X.
    The third line contains n space-separated integers describing the respective elements of array F.
"""

def medianF(N,A):
    """
    Median of array A
    Input: A (array containing numeric values)
           N (length of the array)
    Output: The median of array A"""
    
    sortA = sorted(A)
    halfN = int(N/2)

    if N%2 == 0: #Even number of elements
        h1 = halfN-1 #Python uses 0 indexing, so half-1 and half give median
        h2 = halfN
        return (sortA[h1] + sortA[h2])/2
    
    else: #Odd number of elements
        return sortA[halfN-1]

N = int(input()) #Number of elements in array
A = input().split() #Array of elements
F = input().split() #Array of respective frequencies for elements

A = [int(item) for item in A] #Change values and frequencies to integers
F = [int(item) for item in F]

L = [] #List with values appearing in correspondence to their frequencies
count = 0 #Number of elements in list L

for i in range(N):
    for j in range(F[i]): #Append to list the number of times value appears as frequency
        L.append(A[i])
        count += 1

OrdL = sorted(L)
halfN = int(count/2)

if N%2 == 0: #Even array length
    low = OrdL[:halfN]
    high = OrdL[halfN:]
    
else: #Odd array length
    halfN += 1
    
    low = OrdL[:halfN]
    high = OrdL[halfN+1:]

Q3 = medianF(halfN,low)
Q1 = medianF(halfN,high)

print("{:.1f}".format(float(Q1-Q3)))
    
