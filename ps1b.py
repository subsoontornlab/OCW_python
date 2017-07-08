# this script finds the sum of log(x) when x is a prime number
# less than L. It also compares this sum of log(x) to L.
# The value of sum of log should approach N for large L

from math import *

N = 1000 # number of prime numbers we want to reach
n = 1 # a variable for counting the number of prime we found so far
num = 0 # a number to be tested

sum_of_log = 0

while (n <= N):
    num = num + 1 # go to next testing number
    cnt = 0 # numbers that are not divisor of num
    for t in range(2,num):
        if (num%t == 0):
            break
        cnt = cnt + 1
    if (cnt == num - 2):
        #print(str(num) + " is prime number " + str(n))
        sum_of_log = sum_of_log + log(num)
        print("sum of log = " + str(sum_of_log) + ";ratio = " + str(sum_of_log/num))
        n = n + 1  # count up the number of prime number we have so far
        

