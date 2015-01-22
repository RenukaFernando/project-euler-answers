def function():
    print "Function Called."
    return True

if False and function():
    print "No"

if True or function():
    print "No"
