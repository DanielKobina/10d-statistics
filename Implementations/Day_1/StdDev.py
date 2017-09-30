"""
Objective:
In this challenge, we practice calculating standard deviation. 
    Check out the Tutorial tab for learning materials and an instructional video!

Task:
Given an array, X, of N integers, calculate and print the standard deviation. 
    Your answer should be in decimal form, rounded to a scale of decimal place (i.e., 12.3 format). 
    An error margin of +/- 1 will be tolerated for the standard deviation.

Input Format:
The first line contains an integer, N, denoting the number of elements in the array.
    The second line contains N space-separated integers describing the respective elements of the array.
"""

N = int(input()) #Number of elements in array
A = input().split() #Array of elements
A = [int(x) for x in A] #Change array from strings to integers

avg = sum(A)/N #Average of array
chg = 0

for ele in A:
    sqd = (ele - avg)**2
    chg += sqd
    
std = (chg/N)**(1/2)
print(std)
