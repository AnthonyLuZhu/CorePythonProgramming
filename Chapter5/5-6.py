print  cmp(-6,2)

print cmp(-4.33333, -2.718281828)

print cmp(0xFF, 255)

print str(0xFF)

print str(55.3e2)

print type(0xFF)

print type(98765432109876543210L)

print type(2-1j)

print int(4.25555)

print long (42)

print float(4)

print complex(4)

print complex (2.4, -8)

print complex (2.3e-10, 45.3e4)

print abs(-1)

print (10.0)

print abs(1.2 - 2.1j)

print abs(0.23 - 0.78)

print coerce(1,2)
print coerce(1.3, 134L)


print coerce(1,134L)

print coerce(1j , 134L)

print coerce(1.23 - 41j,134L)

print divmod (10, 3)

print divmod(3, 10)

print divmod(10, 2.5)

print divmod(2.5, 10)

print divmod(2 + 1j, 0.5 - 1j)

print pow(2,5)

print pow(5,2)

print pow(3.141592, 2)

print pow(1+ 1j, 3)

print round(3)

print round(3.45)

print round(3.499999,1)

import math
for eachNum in range(10):
    print round(math.pi, eachNum)

print round(-3.5)

print round(-3.4)

print round(-3.49)

print round(-3.49, 1)

for eachNum in (.2, .7 , 1.2, 1.7, -.2, -.7, -1.2, -1.7):
    print "int (%.1f)\t% +  .1f" % (eachNum, float(int(eachNum)))
    print "floor(%1f)\t% +  1f" % (eachNum, math.floor(eachNum))
    print "round(%1f)\t% +  1f" % (eachNum, round(eachNum))
    print '-' * 20


print hex(255)

print hex(2309482231L)

print oct(255)

print oct(230948231)

print oct(230948231L)

print ord ('a')
print ord ('A')
print ord ('0')
print chr (97)
print chr (65L)
print chr(48)










