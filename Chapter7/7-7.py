s = set('cheeseshop')
t = frozenset('bookshop')
print 'k' in s

print 'k' in t

print 'c' not in t

print  s == t
print s != t
u = frozenset(s)
print s == u
print set('posh') == set('shop')

print set('shop') < set('cheeseshop')

print set('bookshop') >= set('shop')


print s | t

print s & t

print  s - t

print s ^ t

print t | s


