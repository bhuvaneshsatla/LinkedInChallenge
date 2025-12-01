import math
from operator import index

maxdim = [] #stores the sum of dimensions - finding the maximum among these values will give us the maximum dimensions
dim = [] #stores dimensions

n = 2026
nsq = n * n

#a^2 + b^2 + c^2 = 2026^2, wrote this loop to find all possible combinations of a, b, and c that satisfy this equation

for a in range(1, n):

    asq = a * a
    x = nsq - asq #x is 2026^2 - a^2; b^2 + c^2 = x
    bmax = int(math.sqrt(x) - 1) #the maximum value of b should not exceed the (sqaure root of x - 1); the maximum value of b^2 is when c^2 = 1 => x - 1 = b^2

    for b in range(1, bmax):

        bsq = b * b
        y = x - bsq
        c = int(math.sqrt(y))
        csq = c * c

        #checking if b^2 and c^2 are perfect squares adding up to x
        if bsq + csq == x:

            maxdim.append(a + b + c)
            dim.append([a, b, c])

i = maxdim.index(max(maxdim)) #stores the index of the maximum sum of dimensions to reference the same dimensions in the dimensions array
print("Maximum Dimensions: " + str(dim[i]))

L = dim[i][0]
W = dim[i][1]
H = dim[i][2]

sa = 2 * (L * W + W * H + H * L)

print("Maximum Surface Area: " + str(sa))

cubes = L + W + H - math.gcd(L, W) - math.gcd(W, H) - math.gcd(H, L) + math.gcd(L, W, H)
#formula to find number of cubes the ant cuts through

print("Number of cubes cut: " + str(cubes))
