#Mean, Median, Mode

def meanK(A,N):
    """mean of array A"""
    return sum(A)/N

def medianK(A,N):
    """median of array A"""
    sortA = sorted(A)

    if N%2 == 0: #even number of elements
        halfN = N/2
        h1 = int(halfN-1) #Python uses 0 indexing, so half-1 and half give median
        h2 = int(halfN)
        
        return (sortA[h1] + sortA[h2])/2
    
    else: #odd number of elements
        return sortA[N]
    
def modeK(A,N):
    """mode of array A"""
    sortA = sorted(A)
    highC = 0
    highN = 0
    
    for ele in sortA: 
        if sortA.count(ele) > highC:
            highC = sortA.count(ele) #element with highest frequency
            highN = ele
            
    return highN

N = int(input())
arr = input()

arr_spl = arr.split()
num_arr = [int(x) for x in arr_spl] #change array from strings to integers

print(meanK(num_arr,N))
print(medianK(num_arr,N))
print(modeK(num_arr,N))
