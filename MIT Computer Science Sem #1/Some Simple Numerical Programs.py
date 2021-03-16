# PREVIOUS WORKS ON BINARY SEARCH ALGORITHM EFFICIENCY COMPARED TO
# NEWTON RAPHSON METHOD EFFICIENCY NOT INCLUDED.


#def fib(x):
#    """Assumes x an int >= 0
#    Returns Fibonacci of x"""
#    global numFibCalls
#    numFibCalls += 1
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)
#
#def testFib(n):
#    for i in range(n+1):
#        global numFibCalls
#        numFibCalls = 0
#        print('fib of', i, '=', fib(i))
#        print('fib called', numFibCalls, 'times.')
#    
#print(testFib(6))



#nameHandle = open('kids', 'a')
#nameHandle.write('David\n')
#nameHandle.write('Andrea\n')
#nameHandle.close()
#nameHandle = open('kids', 'r')
#for line in nameHandle:
#    print(line[:-1])
#nameHandle.close()



#t1 = ()
#t2 = (1, 'two', 3)
#t3 = (1, )
#print(t1)
#print(t2)
#print(t3)



#t1 = (1, 'two', 3)
#t2 = (t1, 3.25)
#print(t2)
#print((t1 + t2))
#print((t1 + t2)[3])
#print((t1 + t2)[2:5])
#
#def intersect(t1, t2):
#    """Assumes t1 and t2 are tuples
#    Returns a tuple containing elements that are in
#    both t1 and t2"""
#    result = ()
#    for e in t1:
#        if e in t2:
#            result += (e,)
#    return result



#def findExtremeDivisors(n1, n2):
#    """Assumes that n1 and n2 are positive ints
#    Returns a tuple containing the smallest common divisor > 1 and
#    the largest common divisor of n1 and n2. If no common divisor,
#    returns (None, None)"""
#    minVal, maxVal = None, None
#    for i in range(2, min(n1, n2) + 1):
#        if n1%i == 0 and n2%i == 0:
#            if minVal == None:
#                minVal = i
#            maxVal = i
#    return (minVal, maxVal)
#
#print(findExtremeDivisors(5, 6))



#L1 = [1,2,3]
#L2 = [4,5,6]
#L3 = L1 + L2
#print('L3 =', L3)
#L1.extend(L2)
#print('L1 =', L1)
#L1.append(L2)
#print('L1 =', L1)
#
#def removeDups(L1, L2):
#    """Assumes that L1 and L2 are lists.
#    Removes any element from L1 that also occurs in L2"""
#    for e1 in L1:
#        if e1 in L2:
#            L1.remove(e1)
#L1 = [1,2,3,4]
#L2 = [1,2,5,6]
#removeDups(L1, L2)
#print('L1 =', L1)



#def cube(x):
#    x=x**3
#    return x
#
#def applyToEach(L, f):
#    for i in range(len(L)):
#        L[i]=f(L[i])
#
#L=[1, 2, 3, 4, 5]
#print('L= ', L)
#print('Apply cube to each element of L.')
#applyToEach(L, cube)
#print('L= ', L)
#
#def fib(n):
#    """Assumes n int >= 0
#    Returns Fibonacci of n"""
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#
#def testFib(n):
#    for i in range(n+1):
#        print('fib of', i, '=', fib(i))
#
#for i in map(fib, [2, 6, 4]):
#    print(i)
#
#L1 = [1, 36]
#L2 = [2, 57, 9]
#for i in map(min, L1, L2):
#    print(i)
#
#L = []
#for i in map(lambda x, y: x**y, L1, L2):
#    L.append(i)
#print(L)



#def keySearch(L, k):
#    for elem in L:
#        if elem[0] == k:
#            return elem[1]
#    return None



#birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine', 
#'Apr':'Diamond', 'May':'Emerald'}
#months = birthStones.keys()
#print(months)
#birthStones['June'] = 'Pearl'
#print(list(months))



#def copy(L1, L2):
#    """Assumes L1, L2 are lists
#    Mutates L2 to be a copy of L1"""
#    if L1 != L2:
#        while len(L2) > 0: #remove all elements from L2
#            L2.pop() #remove last element of L2
#        for e in L1: #append L1's elements to initially empty L2
#            L2.append(e)
#    else:
#        print("given lists are the same, no copying necessary")
#
#Ly=[1, 3, 5, 7, 9, 11, 13, 15]
#Lz=[2, 4, 6, 8, 10, 12, 14, 16]
#
#print(Lz)
#copy(Ly, Lz)
#print(Lz)



#L=["3", "5", "0", 9]
#def isEven(l): 
#        for i in l: 
#                if i % 2 == 0: 
#                        return i 
#        raise ValueError("No even numbers in list!") 
#print(isEven(L))