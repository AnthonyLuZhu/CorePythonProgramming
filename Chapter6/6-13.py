list1 , list2 = [123,'xyz'], [456,'abc']
a1 = cmp(list1,list2)
print a1
a2 = cmp(list2 ,list1)
print a2

list3 = list2 + [789]

a3 = cmp(list2 , list3)

print a3

s =['They', 'stamp','them','when',"they're", 'small']

for t in reversed(s):
    print t

print sorted(s)

albums = ['tales','robot','pyramid']
for i, album in enumerate(albums):
    print i,album



fn = ['ian','stuart','david']
ln = ['bairnson', 'elliott','paton']

for i , j in zip(fn,ln):
    print ('%s %s' % (i,j)).title()


a = [6,4,5]

print sum(a)

print sum(a,5)

a = [6.,4.,5.]

print sum(a)

aList = ['tao', 93,99,'time']
aTuple = tuple(aList)

print aList,aTuple

print aList == aTuple

anotherList = list(aTuple)

print aList == anotherList

print aList is anotherList

print [id(x) for x in aList,aTuple, anotherList]

