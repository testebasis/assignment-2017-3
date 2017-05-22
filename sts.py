# import sys module
import sys
import random

#the input argument n to Pyhton script
n = sys.argv[1]
n = int(n)

#init lists
numbers = []
list1 = []
list2 = []
dictionary = {}

#function to do list actions
def deleteListElements(diction,theList):
    diction[theList[0]] -= 1
    diction[theList[1]] -= 1
    diction[theList[2]] -= 1
    return theList 
#function to show the results
def showResults(listA,listB):
    print(sorted(listB))
    print(len(listA))
n1 = int(n * (n - 1) / 6)
for i in range(1, n + 1):
    numbers.append(i)
    dictionary[i] = 0
while True:
    if n1 == 0: break
    k = 1
    while k == 1:
        x = random.choice(numbers)
        if(dictionary[x] < (n-1)/2): k = 0
    while k == 0:
        y = random.choice(numbers)
        z = random.choice(numbers)
        if(x == y or y==z or z==x): continue
        for i in range(len(list1)):
            if(x in list1[i] and (y in list1[i] or z in list1[i])): break
        else: k = 1
    for i in range(len(list1)):
        if(y in list1[i] and z in list1[i]):
            list1[i] = deleteListElements(dictionary,list1[i])
            list1.remove(list1[i])
            n1 += 1
            break
    else:
        list1.append([x,y,z])
        dictionary[x] += 1
        dictionary[y] += 1
        dictionary[z] += 1
        n1 -= 1
for i in list1:
    m = tuple(sorted(i))
    list2.append(m)
#show the results
showResults(list1,list2)
