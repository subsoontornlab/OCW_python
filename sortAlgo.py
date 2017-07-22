def selectSort(L):
    for j in range(len(L)):
        minIndx = j
        minVal = L[minIndx]
        for i in range(j, len(L)):
            if L[i] < minVal:
                minIndx = i
                minVal = L[i]
        temp = L[j]
        L[j] = L[minIndx]
        L[minIndx] = temp
        print(L)

        

def bubbleSort(L):
    for j in range(len(L)):
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                print(L)

                
def bubbleSort2(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True
        print(L)


def merge(A, B):
    togetherAB = []
    while (len(A) > 0) & (len(B) > 0):
        if A[0] > B[0]:
            togetherAB.append(B[0])
            del(B[0])
        else:
            togetherAB.append(A[0])
            del(A[0])
        #print(A)
        #print(B)
        #print(togetherAB)
        #print('-------------------')
    if len(A) > 0:
        togetherAB = togetherAB + A
    else:
        togetherAB = togetherAB + B
    return togetherAB

        
        
def mergeSort(L):
    print(L)
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = merge(left, right)
        print('merge ' + str(together))
        return together

def create(smallest, largest): # create an empty list
    intset = []
    for i in range(smallest, largest+1):
        intSet.append(None)
    return intSet

def insert(intSet, e): # add number e to the collection ... so eth position = 1
    intSet[e] = 1

def member(intSet, e):  # check membership
    return intSet[e] == 1

def hashChar(c):
    '''
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord(u'\u2020') returns 8224. 
    '''
    return ord(c)

def cSetCreate():
    cSet = []
    for i in range(0,255): cSet.append(None)
    return cSet

def cSetInsert(cSet, e):
    cSet[hashChar(e)] = 1

def cSetMember(cSet, e):
    return cSet[hashChar(e)] == 1
