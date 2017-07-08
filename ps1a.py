# this script finds and print  1000th prime number

N = 1000 # number of prime numbers we want to reach
n = 1 # a variable for counting the number of prime we found so far
num = 0 # a number to be tested

while (n <= N):
    num = num + 1 # go to next testing number
    cnt = 0 # numbers that are not divisor of num
    for t in range(2,num):
        if (num%t == 0):
            break
        cnt = cnt + 1
    if (cnt == num - 2):
        print(str(num) + " is prime number " + str(n))
        n = n + 1  # count up the number of prime number we have so far
        

