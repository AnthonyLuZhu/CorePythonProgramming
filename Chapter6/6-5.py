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