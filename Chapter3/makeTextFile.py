#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep
fname = 'myTxt.log'

# get filename
while True:
    if os.path.exists(fname):
        print "Error : '%s' already exist" % fname
    else:
        break

# get file content (text) lines

all = []
print "\n Enter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    enter = raw_input('>')
    if enter == '.':
        break
    else:
        all.append(enter)

# write lines to files with proper line -ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all]);
fobj.close();
print 'DONE'
