myDict = {'host':'earth', 'port':80}
print myDict.keys()
print myDict.items()

print myDict.setdefault('port', 80)

print myDict.setdefault('port', 8080)

print myDict.setdefault('prot', 'tcp')

print myDict.items()