"""
Objective:
In this challenge, we practice calculating Spearman's rank correlation coefficient. 
  Check out the Tutorial tab for learning materials!

Task:
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

Input Format:
The first line contains an integer, n, denoting the number of values in data sets X and Y.
The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.
"""

def spearman(rx,ry):
    """Spearman Correlation Coefficient
    Input: rx (rank array of array x)
           ry (rank array of array y)
    Output: Spearman Correlation Coefficient of arrays x and y"""
    n = len(rx)
    d = 0
    for i in range(n):
        d += (rx[i]-ry[i])**2
        
    top = 6 * d
    bot = n * (n**2 - 1)
    
    return 1 - (top/bot)
    
def ranker(arr):
    """Obtain rank of each element in the array
    Input: arr (array of elements)
    Output: array of ranked elements from original array"""
    asort = sorted(arr)
    ret_arr = []
    
    for ele in arr:
        for idx,e2 in enumerate(asort):
            if ele == e2:
                ret_arr.append(idx+1)
                break
                
    return ret_arr

n = int(input())
x = input().split()
x = [float(i) for i in x] #Array x
y = input().split()
y = [float(i) for i in y] #Array y

rx = ranker(x) #Rank array of x
ry = ranker(y) #Rank array of y

rs = spearman(rx,ry) #Spearman Correlation Coefficient

print("{:.3f}".format(rs))
