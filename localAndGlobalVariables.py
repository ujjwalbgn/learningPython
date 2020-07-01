#declearing f vatiable
f =0

# Global vs. local variables in functions
def someFuction():
    global f 
    f="def"
    print(f)

someFuction()
print(f)

del f  #delete f

#with out global f this will print "0" and  "def"
#with global f this will print "def" and "def"