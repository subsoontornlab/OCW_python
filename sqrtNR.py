def squareRootNR(x,epsilon):
    ''' Assumes x >= 0 and epsilon x > 0
        Return y s.t. y*y is within epsilon of x '''
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    x = float(x)
    guess = x/2.0
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'iteration count exceeded'
    print('NR method. Num. iterations: ', ctr, 'Estimate: ', guess)
    return guess

def testBi():
    print('squareRoot(4,0.0001)')
    squareRootBi(4,0.0001)
    print('squareRoot(9,0.0001)')
    squareRootBi(9,0.0001)
    print('squareRoot(2,0.0001)')
    squareRootBi(2,0.0001)    
