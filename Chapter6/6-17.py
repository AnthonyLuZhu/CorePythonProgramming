t = (['xyz',123],23,-103.4)
print t
print t*2
t = t + ('free', 'easy')
print t
print 23 in t
print 123 in t
print t[0][1]
print t[1:]

print str(t)

print len(t)

print max(t)

print min(t)

print cmp(t, (['xyz',123],23,-103.4,'free', 'easy' ))

print list(t)

print (4,2) < (3,5)

print (2,4) < (3,1)

print (2,4) == (3,-1)

print (2,4) == (2,4)