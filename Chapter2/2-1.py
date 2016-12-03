import sys

mystring = 'Hello World!'
print mystring

print "%s is number %d!" % ("Python" , 1)

print >> sys.stderr, 'Fatal Error: invalid input!'

logfile = open('mylog.txt','a')

print >> logfile, 'Fatal Error: invalid input!'

logfile.close()
