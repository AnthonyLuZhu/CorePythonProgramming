person = ['name', ['savings', 100.00]]
hubby = person[:]
wifey = list(person)

print [id(x) for x in person, hubby,wifey]

hubby[0] = 'joe'
wifey[0] = 'jane'

print hubby, wifey

hubby[1][1] = 50.0

print hubby,wifey


person = ['name', ['savings', 100.00]]
hubby = person

import copy
wifey = copy.deepcopy(person)
print [id(x) for x in person, hubby, wifey]
hubby[0] = 'joe'
wifey[0] = 'jane'

print hubby, wifey

hubby[1][1] = 50.0

print hubby,wifey
