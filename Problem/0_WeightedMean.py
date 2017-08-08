N = int(input())
X = input().split()
W = input().split()

X = [int(c) for c in X] #change from strings to integers
W = [int(c) for c in W]

top = 0
bot = 0

for i in range(N): #weighted mean formula
    top += X[i] * W[i] 
    bot += W[i]
   
#print(float(int(top/bot)))
print("{:.1f}".format(top/bot)) #1 decimal point
