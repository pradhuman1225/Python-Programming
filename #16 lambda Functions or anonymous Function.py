# lambda Functions or anonymous Functions
"""
def add (a, b):
    return a+b

# minus = lambda x, y: x-y

def minus (x,y):
    return x-y

print(minus(9,4))
"""


"""def a__first(a):
    return a[1]

a= [[1,14],[4,6],[7,23]]
a.sort(key= a__first)
print(a)
"""

a= [[1,14],[4,6],[7,23]]
a.sort(key= lambda x:x[1])
print(a)
