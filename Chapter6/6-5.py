str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'

print cmp(str1,str2)
print cmp(str3,str1)
print cmp(str2,'lmn')


str1 = 'abc'
print len(str1)
print len('Hello World!')

str2 = 'lmn'
str3 = 'xyz'
print max(str2)
print min(str3)

print min('ab12cd')
print min('AB12CD')
print min('ABabCDcd')

s = 'foobar'
for i, t  in enumerate(s):
    print i,t

user_input = raw_input("Enter your name:")

print user_input
print len(user_input)

print isinstance(u'\0xAB',str)
print  not isinstance('foo', unicode)
print isinstance(u'',basestring)
print not isinstance('foo', basestring)

print chr(65)
print ord('a')
print unichr(12345)



