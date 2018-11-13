
import numpy as np
import timeit as ti
"""
a = [[0,5], [10, 15], [11,100]]
b = [[2,3], [5,4]]
matmu = np.matmul(a,b)

print(matmu)

"""
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
hcMatrix = np.zeros([len(heroes), len(comics)], dtype=np.int8)


print("The length of the heroes list is: " + str(len(heroes)))
print("The length of the comics list is: " + str(len(comics)))



for i in edges:
    asso = 1
    comics = i[1].split()
    for j in comics:
        row = int(i[0]) - 1            #minus 1 since 0 to n-1 indexing
        col = int(j) - 6487         #minus 6487 since 0 to n-1 indexing
        hcMatrix[row][col] = asso


for j in range(0,12941):
    i = 5305
    if(hcMatrix[i][j] == 1):
        print(1, end = "")
print("\n")
