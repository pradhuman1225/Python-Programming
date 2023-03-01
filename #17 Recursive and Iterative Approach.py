# Recursive and Iterative Approach-
# 
"""
def print2(str1):
    print2(str1)
    print("This is " + str1)

print2("Pradhuman")
"""
# Iterative method
"""
def fectorial_iterative (n):
   
    fac = 1
    for i in range(n):
        fac= fac * (i+1)
    return fac
    

number= int(input("Enter the number :"))

print(fectorial_iterative(number))
"""
# Recursive Method

def fectorial_recursive (n):

    if n==1:
        return 1

    else:
        return n * fectorial_recursive(n-1)

number= int(input("Enter the number :"))

print(fectorial_recursive(number))