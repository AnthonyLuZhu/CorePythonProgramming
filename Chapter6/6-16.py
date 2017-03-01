aTuple = (123,'abc',4.56,['inner','tuple'], 7 - 9j)
anotherTuple = (None, 'something to see here')
print aTuple
print anotherTuple

emptiestPossibleTuple  = (None,)
print emptiestPossibleTuple

print tuple('bar')

print aTuple[1:4]
print aTuple[:3]
print aTuple[3][1]

aTuple = aTuple[0], aTuple[1], aTuple[-1]
print aTuple
tup1 = (12,34.56)
tup2 =('abc', 'xyz')
tup3 = tup1 + tup2
print tup3


