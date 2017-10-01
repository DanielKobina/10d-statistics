"""
Objective:
In this challenge, we go further with geometric distributions. 
    We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task:
The probability that a machine produces a defective product is 1/3. 
    What is the probability that the 1st defect is found during the first 5 inspections?

Input Format:
The first line contains the respective space-separated numerator and denominator for the probability of a defect, 
    and the second line contains the inspection we want the probability of the first defect being discovered by:
    1 3
    5
"""

def CDFgeometric(p,k):
    """Geometric Cumulative Distribution function
    equation: 1 - (q)^k    
    
    Input: p (probability of event)
           k (trial number of interest)
    Output: probability of event happening within first k trials"""
    
    q = 1-p
    val = q**k
    return 1-val

num,den = input().split()
num,den = int(num),int(den)

k = int(input()) #Number of inspections we observe
p = num/den #Probability that a machine produces a defective product

output = CDFgeometric(p,k)   
print("{:.3f}".format(output))
