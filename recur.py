def isPalindrome(s):
    '''Return True if s is a palindrome and False otherwise'''
    if len(s) <= 1 : return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def isPalindrome(s, indent):
    '''Return True if s is a palindrome and False otherwise'''
    print(indent + 'isPlaindrome1 called with ' +  s) 
    if len(s) <= 1 :
        print(indent + 'About to return True from base case')
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome(s[1:-1], indent+indent)
        print(indent + 'About to return ' + str(ans))
        return ans

def fib(x):
    ''' Return fibonacci of x, where x is a non-negative int'''
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
