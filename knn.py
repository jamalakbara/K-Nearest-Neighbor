import math
import csv
import numpy as np

def bubbleSort(qont,alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                temp2 = qont[i]
                alist[i] = alist[i+1]
                qont[i] = qont[i+1]
                alist[i+1] = temp
                qont[i+1] = temp2

def bubbleSortB(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1]>alist[i+1][1]:
                temp = alist[i]

                alist[i] = alist[i+1]

                alist[i+1] = temp


def nilEuclidean(dataTrain, dataTest,a):
    ind = []
    euclidean = []
    for idx in range(0,len(dataTrain[0])):
        jum = 0
        for i in range(1, len(dataTrain) - 1):
            z = pow(dataTrain[i][idx] - dataTest[i][a], 2)
            jum = jum + z
        rumus = math.sqrt(jum)
        ind.append(int(idx+1))
        euclidean.append(float(rumus))
    euIndex = [ind,euclidean]
    return  euIndex

def slice(list, k):
    global potong
    # potong = []
    potong.clear()
    for i in range(0, k):
        potong.append(list[0][0:k][i])

    return potong


def itungKlasifikasi(dataTrain, k):
    global count0
    global count1
    global count2
    global count3
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(0, k):
        if (dataTrain[6][potong[i]-1] == 0):
            count0 += 1
        elif (dataTrain[6][potong[i]-1] == 1):
            count1 += 1
        elif (dataTrain[6][potong[i]-1] == 2):
            count2 += 1
        elif (dataTrain[6][potong[i]-1] == 3):
            count3 += 1

    return count1,count2,count3

with open('DataTrain_Tugas3_AI.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    idx = []
    xTrain1 = []
    xTrain2 = []
    xTrain3 = []
    xTrain4 = []
    xTrain5 = []
    yTrain = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # dTrain.append([int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),int(row[6])])
            idx.append(int(row[0]))
            xTrain1.append(float(row[1]))
            xTrain2.append(float(row[2]))
            xTrain3.append(float(row[3]))
            xTrain4.append(float(row[4]))
            xTrain5.append(float(row[5]))
            yTrain.append(int(row[6]))

dataTrain = [idx,xTrain1,xTrain2,xTrain3,xTrain4,xTrain5,yTrain]

with open('DataTest_Tugas3_AI.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    index = []
    xTest1 = []
    xTest2 = []
    xTest3 = []
    xTest4 = []
    xTest5 = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # dTest.append([int(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])])
            index.append(int(row[0]))
            xTest1.append(float(row[1]))
            xTest2.append(float(row[2]))
            xTest3.append(float(row[3]))
            xTest4.append(float(row[4]))
            xTest5.append(float(row[5]))

dataTest = [index,xTest1,xTest2,xTest3,xTest4,xTest5]
def findPersenK(k):
    with open('DataTrain_Tugas3_AI.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        dTrain = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                dTrain.append([int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),int(row[6])])

    np.random.shuffle(dTrain)
    split = int(math.floor(len(dTrain)/2))

    testNew = dTrain[0:split]
    trainingNew = dTrain[split:]

    idxAnyar = []
    x1Anyar = []
    x2Anyar = []
    x3Anyar = []
    x4Anyar = []
    x5Anyar = []
    for i in range(0,len(testNew)):
        idxAnyar.append(testNew[i][0])# = [testNew[i][0],testNew[i][0],testNew[i][0]]
        x1Anyar.append(testNew[i][1])
        x2Anyar.append(testNew[i][2])
        x3Anyar.append(testNew[i][3])
        x4Anyar.append(testNew[i][4])
        x5Anyar.append(testNew[i][5])

    dataTestAnyar = [idxAnyar,x1Anyar,x2Anyar,x3Anyar,x4Anyar,x5Anyar]

    indexAnyar = []
    xx1Anyar = []
    xx2Anyar = []
    xx3Anyar = []
    xx4Anyar = []
    xx5Anyar = []
    yAnyar = []
    for i in range(0,len(trainingNew)):
        indexAnyar.append(trainingNew[i][0])# = [testNew[i][0],testNew[i][0],testNew[i][0]]
        xx1Anyar.append(trainingNew[i][1])
        xx2Anyar.append(trainingNew[i][2])
        xx3Anyar.append(trainingNew[i][3])
        xx4Anyar.append(trainingNew[i][4])
        xx5Anyar.append(trainingNew[i][5])
        yAnyar.append(trainingNew[i][6])

    dataTrainAnyar = [indexAnyar,xx1Anyar,xx2Anyar,xx3Anyar,xx4Anyar,xx5Anyar,yAnyar]


    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    fix = []

    for i in range(0,len(dataTest[0])):
        euIndex = nilEuclidean(dataTrain,dataTest,i)
        bubbleSort(euIndex[0],euIndex[1])

        potong = slice(euIndex,k)

        itungKlasifikasi(dataTrain,k)
        if (count0 > 0) and (count0 > count1 and count0 > count2 and count0 > count3):
            fix.append(int(0))
        elif (count1 > 0) and (count1 > count0 and count1 > count2 and count1 > count3):
            fix.append(int(1))
        elif (count2 > 0) and (count2 > count1 and count2 > count0 and count0 > count3):
            fix.append(int(2))
        elif (count3 > 0) and (count3 > count1 and count3 > count2 and count3 > count0):
            fix.append(int(3))
        else:
            fix.append(int(dataTrain[6][potong[0]-1]))

    #     print('loading',i/4,'%')
    #
    # print('loading 100 %')
    countPersen = 0
    for i in range(0, len(trainingNew)):
        if (fix[0] == trainingNew[i][6]):
            countPersen += 1
    persen = (countPersen / 400) *100
    # print(persen)
    return  persen


print('PLEASE WAIT A LITTLE LONGER....')
print('SYSTEM IS SEARCHING FOR BEST K TO USE')
print("THIS WON'T BE LOOPING FOREVER... I SWEAR......")
print('APPROXIMATELY NEED 3-8 MIN..')
print('SORRY, THIS ALGORITHM MADE BY OWNSELF..')
print('SO THIS ALGORITHM MAY NOT EFFICIENT :)')
potong = []
kNotFix = []
for perc in range(3,20):
    if (perc%2 == 1) :
        p = findPersenK(perc)
        kNotFix.append([perc, p])

bubbleSortB(kNotFix)
# print('BEST K FOUND',kNotFix)

count0 = 0
count1 = 0
count2 = 0
count3 = 0
fix = []
k = kNotFix[8][0]

for i in range(0,len(dataTest[0])):
    euIndex = nilEuclidean(dataTrain,dataTest,i)
    bubbleSort(euIndex[0],euIndex[1])

    potong = slice(euIndex,k)

    itungKlasifikasi(dataTrain,k)
    if (count0 > 0) and (count0 > count1 and count0 > count2 and count0 > count3):
        fix.append(int(0))
    elif (count1 > 0) and (count1 > count0 and count1 > count2 and count1 > count3):
        fix.append(int(1))
    elif (count2 > 0) and (count2 > count1 and count2 > count0 and count0 > count3):
        fix.append(int(2))
    elif (count3 > 0) and (count3 > count1 and count3 > count2 and count3 > count0):
        fix.append(int(3))
    else:
        fix.append(int(dataTrain[6][potong[0]]))

    print('loading',i/2,'%')

with open('TebakanTugas3.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    for idx in range(0,len(fix)):
        csv_writer.writerow([fix[idx]])

print('loading 100 %')
print('K Used = ',kNotFix[8][0])
print('TebakanTugas3.csv saved successfully')
print('THANK YOU FOR WAITING!!!')