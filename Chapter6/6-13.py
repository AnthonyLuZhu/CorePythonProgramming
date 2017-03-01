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