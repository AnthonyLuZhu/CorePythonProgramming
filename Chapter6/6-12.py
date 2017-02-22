list1 = ['abc',123]
list2 = ['xyz',789]
list3 = ['abc', 123]

print  list1 < list2

print  list2 < list3

print list2 > list3 and list1 == list3

num_list = [43,-1.23,-2, 6.19e5]
str_list = ['jack', 'jumped','over','candlestick']
mixup_list = [4.0,[1,'x'],'beef',-1.9+6j ]

print num_list[1]

print num_list[1:]

print num_list[2:-1]

print str_list[2]

print str_list[:2]

print mixup_list

print mixup_list[1]

print mixup_list[1][1]

mixup_list[1][1]=-64.875

print mixup_list

print num_list

num_list[2:4] = [16.0, -49]

print num_list

num_list[0] = [64535L, 2e30, 76.45-1.3j]

print num_list

print mixup_list

print 'beef' in mixup_list

print 'x' in mixup_list

print  num_list

print  -49 in num_list

print 34 in num_list

print [64535L, 2e30, 76.45-1.3j] in num_list

print num_list + mixup_list
print str_list + num_list

print num_list * 2

print num_list * 3

print [i * 2 for i in [8,-2,5]]
print [i for i in range(8) if i % 2 == 0]


