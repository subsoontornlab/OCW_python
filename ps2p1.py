# this script prints out a, b, c which satisfies
# 6*a + 9*b + 20*c = n
# when n is 50, 51, 52, 53, 54, 55

n = int(input("Please enter the total amount of nuggets: "))

max_6 = int(n/6)
max_9 = int(n/9)
max_20 = int(n/20)

solList = []

for a in range(0,max_6+1):
    for b in range(0,max_9+1):
        for c in range(0, max_20+1):
            #print([a,b,c])
            #print(6*a + 9*b + 20*c)
            if (6*a + 9*b + 20*c == n):

                print("Found "+ str([a,b,c]) + "!!")
                solList.append([a,b,c])

if len(solList) < 1 :
    print("No solution found")
else:
    print("Here are all solutions:")
    print(solList)



