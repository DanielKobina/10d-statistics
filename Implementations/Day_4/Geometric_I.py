"""
Objective:
In this challenge, we go further with geometric distributions. 
    We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task:
The probability that a machine produces a defective product is 1/3. 
    What is the probability that the 1st defect is found during the 5th inspection?

Input Format:
The first line contains the respective space-separated numerator and denominator for the probability of a defect, 
    and the second line contains the inspection we want the probability of the first defect being discovered by:
    1 3
    5
"""

def geometric(p,k):
    """Geometric Mass Distribution function
    equation: [q ^ (k-1)] * p
    
    Input: p (probability of event)
           k (number of trials considering)
    Output: probability of function"""
    
    q = 1-p
    return q**(k-1) * p

num,den = input().split()
num,den = int(num),int(den)

k = int(input()) #Number of inspections we observe
p = num/den #Probability that a machine produces a defective product


output = geometric(p,k)
print("{:.3f}".format(output))
