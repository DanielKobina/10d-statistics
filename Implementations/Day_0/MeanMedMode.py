"""
Objective:
In this challenge, we practice calculating the mean, median, and mode. 
    Check out the Tutorial tab for learning materials and an instructional video!

Task:
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
    If your array contains more than one modal value, choose the numerically smallest one.

Note: 
Other than the modal value (which will always be an integer), your answers should be in decimal form, 
    rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).

Input Format:
The first line contains an integer, N, denoting the number of elements in the array.
    The second line contains N space-separated integers describing the array's elements.
"""

def meanK(A,N):
    """
    Mean of array A
    Input: A (array containing numeric values)
           N (length of the array)
    Output: The mean of array A"""
    
    return sum(A)/N

def medianK(A,N):
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
    
def modeK(A,N):
    """
    Mode of array A
    Input: A (array containing numeric values)
           N (length of the array)
    Output: The mode of array A"""
    
    sortA = sorted(A) #If multimodal array, takes smallest number as mode
    highC = 0
    highN = 0
    
    for ele in sortA: 
        if sortA.count(ele) > highC:
            highC = sortA.count(ele) #Element with highest frequency
            highN = ele #Highest frequency
            
    return highN

N = int(input())
arr = input().split()

num_arr = [int(x) for x in arr] #Change array from strings to integers

print("{:.1f}".format(meanK(num_arr,N)))
print("{:.1f}".format(medianK(num_arr,N)))
print(modeK(num_arr,N))
