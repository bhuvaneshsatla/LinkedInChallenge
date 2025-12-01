import math
from operator import index

maxdim = []
dim = []
sa = []

n = 2026
nsq = n * n

for a in range(1, n):

    asq = a * a
    x = nsq - asq
    bmax = int(math.sqrt(x))

    for b in range(1, bmax):

        bsq = b * b
        y = x - bsq
        c = int(math.sqrt(y))
        csq = c * c

        if bsq + csq == x:

            maxdim.append(a + b + c)
            dim.append([a, b, c])
            sa.append((2 * (a * b + b * c + c * a)))

i = maxdim.index(max(maxdim))
print("Maximum Dimensions: " + str(dim[i]))
print("Maximum Surface Area: " + str(sa[i]))

L = dim[i][0]
W = dim[i][1]
H = dim[i][2]

cubes = L + W + H - math.gcd(L, W) - math.gcd(W, H) - math.gcd(H, L) + math.gcd(L, W, H)
print("Number of cubes cut: " + str(cubes))