# code for OCW python lecture 8

def exp1(a,b): # iterative
    ans = 1
    while (b>0):
        ans *= a
        b -= 1
    return ans

def exp2(a,b): # recursive
    if b == 1:
        return a
    else: return a*exp2(a,b-1)

def exp3(a,b): # recursive branch
    if b == 1:
        return a
    if (b%2)*2 == b: # by is even
        return exp3(a*a, b/2)
    else: return a*exp3(a,b-1)

    
