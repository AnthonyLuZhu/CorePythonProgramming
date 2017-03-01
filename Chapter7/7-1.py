dict1 = {}
dict2 = {'name': 'earth', 'port' : 80}

print dict1, dict2

fdict = dict((['x',1],['y',2]))
print fdict

ddict = {}.fromkeys(('x', 'y'), -1)
print ddict

edict = {}.fromkeys(('foo', 'bar'))
print edict

dict2 = {'name': 'earth', 'port' : 80}
for key in dict2.keys():
    print 'key=%s, value=%s' % (key, dict2[key])


dict2 = {'name': 'earth', 'port' : 80}
for key in dict2:
    print 'key=%s, value=%s' % (key, dict2[key])


print 'server' in dict2

print 'name' in dict2

dict3 = {}
dict3[1] = 'abc'
dict3['1'] = 3.14
dict3[3.2] = 'xyz'
print dict3

dict2['name'] == 'venus'
dict2['port'] = 6969
dict2['arch'] = 'sunos5'

print dict2


