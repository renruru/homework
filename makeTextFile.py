#!/usr/bin/env python

# 'makeTextFile.py -- creat text file'

import os
ls = os.linesep

fname = "D:/a.txt"
#get filename
while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exits" % fname
    else:
        break

all = []
print "\nEnter lines ('.'by itself to quit).\n "

while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DOWN!'






            
        

