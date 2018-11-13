
import numpy as np
import time as ti
np.set_printoptions(threshold=8000)
a = [[0,5,3], [10, 15,1], [11,100,7]]
b = [[2,3], [5,4]]
a = np.matrix(a)
b = np.matrix(b)


matmu1 = np.matmul(a,a)
print(matmu1)

matmu2 = a * a
print(matmu2)
#6486 charaters
#spiderman 5306

heroes = []
comics = []
edges = []
i = 1

with open("porgat.txt", "r", encoding="cp1252") as f:       #
    next(f)
    for line in f:
        line = line.strip()
        line = line.split(" ", 1)
        if i <= 6486:
            heroes.append(tuple(line))      #read in heroes as a list of tuples
            i += 1
        elif i <= 19428:
            comics.append(tuple(line))      #read in comics as a list of tuples
            i += 1
        else:
            edges.append(tuple(line))       #read in edges as a list of tuples

f.close()
edges.remove(('*Edgeslist',))
hcMatrix = np.zeros([len(heroes), len(comics)], dtype=np.int32)


print("The length of the heroes list is: " + str(len(heroes)))
print("The length of the comics list is: " + str(len(comics)))



for i in edges:
    asso = 1
    com = i[1].split()
    for j in com:
        row = int(i[0]) - 1            #minus 1 since 0 to n-1 indexing
        col = int(j) - 6487         #minus 6487 since 0 to n-1 indexing
        hcMatrix[row][col] = asso
for j in range(0,len(comics)):
    i = 5305
    if(hcMatrix[i][j] == 1):
        print(1, end = "")
print("\n")
 #end of association matrix

 #start collab matrix
#clbMat = np.zeros([len(heroes),len(heroes)], dtype=np.int8)
""" Collab matrix built, stored in matfile.txt. Building takes ~150s, loading from file takes 20s
t0 = ti.time()
for col in range(0,len(comics)):
    clbHero = []
    for row in range(0,len(heroes)):
        if hcMatrix[row][col] == 1:
            clbHero.append(row)
    for i in clbHero:
        for j in clbHero:
            clbMat[i][j] = 1
t1 = ti.time()
print(clbMat)
totTime = t1 - t0
print("Total time to build collab matrix: " + str(totTime))
savClbMat = np.matrix(clbMat)
with open('matfile.txt', 'w') as f:
    for line in savClbMat:
        np.savetxt(f, line, fmt='%i')
"""
t0 = ti.time()
with open('matfile.txt', 'r') as f:
    clbMat = np.loadtxt(f, dtype=np.int32)
t1 = ti.time()
print(clbMat)
totTime = t1 - t0
print("Total time to build collab matrix: " + str(totTime))
print(clbMat[5305])
spidey2 = np.zeros([len(heroes), len(heroes)], dtype=np.int32)
t0 = ti.time()
print("getting spiderman of 2")
spidey1 = clbMat[5305]
spidey2 = np.matmul(clbMat,spidey1)
print("getting spiderman of 3")
spidey3 = np.matmul(clbMat,spidey2)
print("getting spiderman of 4")
spidey4 = np.matmul(clbMat,spidey3)

t1 = ti.time()
"""
print("spidey 2")
print(spidey2[5305])
print("spidey 3")
print(spidey3[5305])
print("spidey 4")
print(spidey4[5305])
"""
print(spidey1)
print(spidey2)
print(spidey3)
print(spidey4)

totTime = t1-t0
print("Total time for matmul: " + str(totTime))

print("spidey1")
zeroTot = 0
for i in range(0, len(heroes)):
    if spidey1[i] == 0:
        zeroTot += 1
print(zeroTot)
zeroTot = 0
print("spidey2")
for i in range(0, len(heroes)):
    if spidey2[i] == 0:
        zeroTot += 1
print(zeroTot)
zeroTot = 0
print("spidey3")
for i in range(0, len(heroes)):
    if spidey3[i] == 0:
        zeroTot += 1

print(zeroTot)
zeroTot = 0
print("spidey4")
for i in range(0, len(heroes)):
    if spidey4[i] == 0:
        zeroTot += 1

print(zeroTot)


"""
spidey2Mat = np.matrix(spidey2)
with open('matfile1.txt', 'w') as f:
    for line in spidey2Mat:
        np.savetxt(f, line, fmt='%i')

spidey3Mat = np.matrix(spidey3)
with open('matfile1.txt', 'w') as f:
    for line in spidey3Mat:
        np.savetxt(f, line, fmt='%i')

spidey4Mat = np.matrix(spidey4)
with open('matfile1.txt', 'w') as f:
    for line in spidey4Mat:
        np.savetxt(f, line, fmt='%i')
"""
