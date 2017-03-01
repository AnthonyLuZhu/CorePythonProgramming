dict1 = {}
dict2 = {'host':'earth', 'port' : 80}

print cmp(dict1, dict2)

dict1['host'] = 'earth'
print  cmp(dict1, dict2)

dict1['port'] = 8080
print cmp(dict1,dict2)


dict1['port'] = 80
print cmp(dict1,dict2)

dict1['prot'] = 'tcp'
print cmp(dict1,dict2)

dict2['prot'] = 'udp'
print cmp(dict1,dict2)

cdict = {'fruits':1}
ddict = {'fruits':1}
print cmp(cdict, ddict)

cdict['oranges'] = 0
ddict['apples'] = 0
print cmp(cdict, ddict)

print dict(zip(('x','y'), (1,2)))
print dict([['x',1],['y',2]])

print dict([('xy'[i-1], i) for i in range(1,3)])

print dict(x=1,y=2)
dict8 = dict(x=1,y=2)
print dict8
dict9 = dict8.copy()

dict2 = {'name': 'earth', 'port':80}
print len(dict2)

