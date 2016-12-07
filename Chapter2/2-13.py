print 'I like to use the internet for: '

for item in ['e-mail','net-surfing', 'homework','char']:
    print item



print 'I like to use the internet for: '

for item in ['e-mail','net-surfing', 'homework','char']:
    print item,

print


who =  'knights'

what= 'Ni'

print 'We are the ', who ,  'who say' , what , what , what, what

print 'We are the %s who say %s' % (who, ((what + ' ') * 4))

for eachNum in [1,2,3]:
    print eachNum


for eachNum in  range(3):
    print eachNum


foo = 'abc'
for o in foo:
    print o

foo = 'abc'
for i in range(len(foo)):
    print foo[i], '(%d)' % i


print


for i, ch in enumerate(foo):
    print ch,  '(%d)' % i