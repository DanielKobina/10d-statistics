"""
Objective:
In this challenge, we go further with Poisson distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task:
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
    The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
      The daily cost of operating A is Ca = 160 + 40x^2.
    The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
      The daily cost of operating B is Cb = 128 + 40y^2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly
  to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

Input Format:
A single line comprised of space-separated values denoting the respective means for A and B:
  0.88 1.55
"""

A,B = input().split() 
A,B = float(A),float(B) #Expected daily costs of machine A and B respectively

#For Poisson distribution, E(X^2) = u + u^2, where u is the mean value (expected cost)
#adding a constant increases the random variable by addition of the constant
#multiplying a constant increases the random variable by multiplication of the constant
EA = 160 + 40 * (A + (A**2))
EB = 128 + 40 * (B + (B**2))

print(round(EA,3)) #Expected daily cost of machine A
print(round(EB,3)) #Expected daily cost of machine B
