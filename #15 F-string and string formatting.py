# F-strings and strings formatting

import math
me = "Pradhuman"
a1 = 3
# a = "this is %s"%me
# a = "this is %s %s" %(me,a1)
# a = "this is {1} {0}"
#b = a.format(me,a1)
#print(b)

a = f"this is {me} {a1} {math.cos(45)}"
print(a)
