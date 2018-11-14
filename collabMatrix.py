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
