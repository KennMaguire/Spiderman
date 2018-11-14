
import numpy as np
import time as ti

spideyVal = 5305
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

#building association matrix
for i in edges:
    asso = 1
    com = i[1].split()              #
    for j in com:
        row = int(i[0]) - 1            #minus 1 since 0 to n-1 indexing
        col = int(j) - 6487         #minus 6487 since 0 to n-1 indexing
        hcMatrix[row][col] = asso   #if hero is in comic, add 1 to hc matrix
print("\n")
 #end of association matrix

 #start collab matrix
#clbMat = np.zeros([len(heroes),len(heroes)], dtype=np.int8)
""" Collab matrix built, stored in matfile.txt. Building takes ~150s, loading from file takes 20s
t0 = ti.time()
for col in range(0,len(comics)):                    #outer loop goes through all comics, inner loop searchs for associations, if found add to array
    clbHero = []                                    #array for holding values where collab is found
    for row in range(0,len(heroes)):
        if hcMatrix[row][col] == 1:                 #if 1 is found add to list of heroes who were in that comic
            clbHero.append(row)
    for i in clbHero:                               #add 1 for all heroes who appeared in the same comic in the collab matrix using list of heroes who appeared in that comic
        for j in clbHero:
            clbMat[i][j] = 1
t1 = ti.time()
print(clbMat)
totTime = t1 - t0
print("Total time to build collab matrix: " + str(totTime))
savClbMat = np.matrix(clbMat)                       #save matrix to file to lessen load time
with open('matfile.txt', 'w') as f:
    for line in savClbMat:
        np.savetxt(f, line, fmt='%i')
"""
t0 = ti.time()
with open('matfile.txt', 'r') as f:                 #get collab matrix from file
    clbMat = np.loadtxt(f, dtype=np.int32)



t1 = ti.time()
print(clbMat)

totTime = t1 - t0
print("Total time to build collab matrix: " + str(totTime))
print(clbMat[spideyVal])
#spidey2 = np.zeros([len(heroes), len(heroes)], dtype=np.int32)
t0 = ti.time()
print("getting spiderman of 2")
spidey1 = clbMat[spideyVal]                         #creates array of heroes with spidey number of 1
spidey2 = np.matmul(clbMat,spidey1)                 #get array with spidey number of 2 (also has 1 for now)
print("getting spiderman of 3")
spidey3 = np.matmul(clbMat,spidey2)                 #get array with spidey number of 3 (also has 1 and 2 for now)
print("getting spiderman of 4")
spidey4 = np.matmul(clbMat,spidey3)                 #get array with spidey number of 4 (also has 1,2,3 for now)

t1 = ti.time()
"""
print("spidey 2")
print(spidey2[spideyVal])
print("spidey 3")
print(spidey3[spideyVal])
print("spidey 4")
print(spidey4[spideyVal])
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


for i in range(0, len(heroes)):
    if (spidey1[i] > 0 and spidey2[i] > 0) or spidey2[i] == 0:              #remove all values that already have spidey number of 1, from array of heroes wiht spidey # of 2
        spidey2[i] = -1
for i in range(0, len(heroes)):
    if (spidey1[i] > 0 or spidey2[i] > 0) and spidey3[i] > 0:               #remove all values that already have spidey number of 1 or 2, from array of heroes wiht spidey # of 3
        spidey3[i] = -1
for i in range(0, len(heroes)):
    if (spidey1[i] > 0 or spidey2[i] > 0 or spidey3[i] > 0) > 0 and spidey4[i] > 0:  #remove all values that already have spidey number of 1 or 2 or 3, from array of heroes wiht spidey # of 4
        spidey4[i] = -1

spidey1[5305] = 0           #set spiderman to have spidey number of 0 for all arrays
spidey2[5305] = 0
spidey3[5305] = 0
spidey4[5305] = 0
"""
print("spidey1")
for i in range(0, len(heroes)):
    if spidey1[i] > 0:
        print(spidey1[i])
print("spidey2")
for i in range(0, len(heroes)):
    if spidey2[i] > 0:
        print(spidey2[i])
print("spidey3")
for i in range(0, len(heroes)):
    if spidey3[i] > 0:
        print(spidey3[i])
print("spidey4")
for i in range(0, len(heroes)):
    if spidey4[i] > 0:
        print(spidey4[i])

"""
inInd1 = 0
inInd2 = 0
properRange = False

while properRange == False:
    print("Please enter the index you would like to start printing heroes (From 1-6486)")
    inInd1 = int(input())
    print("Please enter the index you would like to finish printing heroes (From 1-6486)")
    inInd2 = int(input())

    inInd1 = inInd1 - 1
    if (inInd1 > -1 and inInd1 < 6486) and (inInd2 > 1 and inInd2 < 6487):
        properRange = True
    else:
        print("outside the range of indexes")
        properRange = False

#get all heroes with spiderman number of 1
for i in range(inInd1, inInd2):           #print in range specified
    heroInd = i
    if spidey1[i] > 0:
        print(heroes[heroInd][1] + " 1")
    elif spidey2[i] > 0:
        print(heroes[heroInd][1] + " 2")
    elif spidey3[i] > 0:
        print(heroes[heroInd][1] + " 3")
    elif spidey2[i] == 0:
        print(heroes[heroInd][1] + " 0")
    else:
        print(heroes[heroInd][1] + " none")






print("spidey1")
zeroTot = 0
for i in range(0, len(heroes)):
    if spidey1[i] != 0:     #0 since spidey1 is 0 or 1
        zeroTot += 1
print(zeroTot)
zeroTot = 0
print("spidey2")
for i in range(0, len(heroes)):
    if spidey2[i] != -1:
        zeroTot += 1
print(zeroTot)
zeroTot = 0
print("spidey3")
for i in range(0, len(heroes)):
    if spidey3[i] != -1:
        zeroTot += 1

print(zeroTot)
zeroTot = 0
print("spidey4")
for i in range(0, len(heroes)):
    if spidey4[i] != -1:
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
