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
