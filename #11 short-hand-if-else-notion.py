"""
a=int(input("Enter a\n"))
b=int(input("Enter b\n"))
if a>b: 
    print("A B se bada hai")
else: 
    print("B A se bada hai")

"""

# short these program.

a=int(input("Enter a\n"))
b=int(input("Enter b\n"))

print("B A se bada hai") if a<b else print("A B se bada hai")
