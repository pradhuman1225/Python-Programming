
"""
a=9
b=8
c=sum((a,b)) # this is build-in function.
print(c)

"""

# now build function.

#def function1():
#    print("Hello python world")

#function1()

#def function2(a,b):
#    print("Hello!!! You print :",a+b)
    
#function2(5,7)

def function3(a,b):

    """This is a function which will calculate average of two number"""

    average=(a+b)/2
    #print(average)
    return average
function3(5,7)

v= function3(5,7)
print(v)

print(function3.__doc__)