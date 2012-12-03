# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...

    sum = 0

    if isinstance(poly,list):
        n = len(poly)

        print n

        for i in range(n):
            print poly[i]*(x**i)
            sum += poly[i]* (x**i)

        return float(sum)

        

    








# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...

    sum = 0
    deriv = []

    if isinstance(poly,list):
        n = len(poly)

        if n == 1:
            deriv = [0.0]
        
        for i in range(n):
            

            if not i == 0:
                deriv.append(float(poly[i]* i) )

        return  deriv





# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...

    n = 1
    x = x_0

    list = []

    while abs(evaluatePoly(poly,x)) > epsilon:

        nom = evaluatePoly(poly,x)
        denom = evaluatePoly(computeDeriv(poly),x)
        
        x = x - (nom/denom)
        
        print "x is %s" % x
        n = n+1
        print "interation number %s" % n

    list.append(float(x))
    list.append(n)

    return list

    
        
