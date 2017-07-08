# this script find the largest integer N which cannot be written
# as the sum of non-negative integer [X,Y,Z]

# this script can be used for both problem 3 and 4 of problem set 2

#NN = int(input("Please enter the total amount of nuggets: "))

# get the sizes of nuggest set .. 6, 9 20 pieces by default
s = input("Please enter the sizes of nugget sets: ") 
list_xyz = list(map(int, s.split()))

X = list_xyz[0]
Y = list_xyz[1]
Z = list_xyz[2]
    
# this function check if n can be written as sum of X, Y, Z
def checkSum(n, listXYZ):

    X = listXYZ[0]
    Y = listXYZ[1]
    Z = listXYZ[2]
    
    max_X = int(n/X)
    max_Y = int(n/Y)
    max_Z = int(n/Z)

    sumXYZexist = False   
    for a in range(0, max_X+1):
        for b in range(0, max_Y+1):
            for c in range(0, max_Z+1):
                if (a*X + b*Y + c*Z == n):
                    sumXYZexist = True
                    #print([a, b, c])
                    break       
    return sumXYZexist

# number to be tested, starting from 1
testNum = 1
# counting the consecutive integers that can be written as a sum of a b c
conCount = 0
# maximum integer N that cannot be written as a sum of a b c
maxN = -1

while conCount < 6:
    sumXYZexist = checkSum(testNum, list_xyz)
    if sumXYZexist:
        conCount = conCount + 1
        print("***Testing number: " + str(testNum) + " has a b c ***")
    else:
        conCount = 0
        maxN = testNum
        print("Testing number: " + str(testNum) + " has NO a b c")
        
    testNum = testNum + 1

print("Given package sizes " + str(X) + ", " + str(Y) + ", and " + str(Z))      
print(", the largest number of McNuggets that cannot be bought in exact quantity: " + str(maxN))




