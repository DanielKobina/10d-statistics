"""
Objective
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of decimal place (i.e., format). An error margin of will be tolerated for the standard deviation.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains space-separated integers describing the respective elements of the array.
"""

N = int(input())
A = input().split()
A = [int(x) for x in A] #change from strings to integers

avg = sum(A)/N #average
chg = 0

for ele in A:
    sqd = (ele - avg)**2
    chg += sqd
    
std = (chg/N)**(1/2)
print(std)
