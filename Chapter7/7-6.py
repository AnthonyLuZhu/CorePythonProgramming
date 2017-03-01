s = set('cheeseshop')
print s

t = frozenset('bookshop')
print t

print type(s)
print type(t)

print len(s)
print len(s) == len(t)
print  s == t

print 'k' in s
print 'k' in t


print 'c' not in t

for i in s:
    print i

s.add('z')
print s

s.update('pypi')
print s

s.remove('z')
print s

s -= set('pypi')
print s
