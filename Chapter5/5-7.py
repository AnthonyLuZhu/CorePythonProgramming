print bool (1)
print bool(True)
print bool(0)
print bool('1')
print bool('0')
print bool([])
print bool((1,))

foo = 42
bar = foo  < 100
print bar

print  bar  + 100

print '%s' % bar

print '%d' % bar

class C : pass

c = C()

print bool(c)

class D:
    def __nonzero__(self):
        return False

d = D()

print bool(d)

print bool(D)

print 0.1

from decimal import Decimal

dec = Decimal('.1')
print dec

print dec + Decimal('1.0')






