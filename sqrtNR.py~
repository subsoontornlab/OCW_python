def squareRootBi(x,epsilon):
    ''' Assumes x >= 0 and epsilon x > 0
        Return y s.t. y*y is within epsilon of x '''
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = max(x,1) #if x>1, sqrt(x) < x ..but if x<1, sqrt(x) > x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('Bi method. Num. iterations: ', ctr, 'Estimate: ', guess)
    return guess

def testBi():
    print('squareRoot(4,0.0001)')
    squareRootBi(4,0.0001)
    print('squareRoot(9,0.0001)')
    squareRootBi(9,0.0001)
    print('squareRoot(2,0.0001)')
    squareRootBi(2,0.0001)    
