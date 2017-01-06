str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'
print (str1 < str2)

print (str2 != str3)

print (str1 < str3 and str2 == 'xyz')

aString = 'abcd'
print len(aString)

print aString[0]

print aString[1:3]

print aString[2:4]

print aString[-1]

print aString[-3: -1]

print aString[-4]

print ('bc' in 'abcd')
print 'n' in 'abcd'
print 'nm' not in 'abcd'

print 'Spanish' + 'Inquistion'

print 'Spanish' + ' '+'Inquistion'

s = 'Spanish' + ' ' + 'Inquistion' + ' Made Easy'
print s

import string
print string.upper(s[:3] + s[20])

print '%s %s' % ('Spanish','Inquistion')

s = ' '.join(('Spanish', 'Inquistion', 'Made Easy'))
print s

print ('%s%s' % (s[:3],s[20])).upper();

foo = "Hello" "world"
print foo

print 'Hello' + u' '+ 'World' + u' '

print 'Ni!' * 3

print '*' * 40

print  '-' * 20, 'Hello World!', '-' * 20

who = 'knights'
print who * 2