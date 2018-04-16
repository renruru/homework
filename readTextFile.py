fname = raw_input("Enter filename:")
print

try:
    fobj = open(fname,'r')
except IOError,e:
    print"***file open Error:",e
else:
    for eachLine in fobj:
        print eachLine
    fobj.close