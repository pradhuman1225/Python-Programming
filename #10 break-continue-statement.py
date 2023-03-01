"""
i=0

while (True):
    if i+1<5:
        i= i+1
        continue
    
    print(i+1)
    if (i==44):
        break
    i = i + 1 
"""
# print the given number by user. when entered the number greater than 100 print - congrats
# when entered les than 100 print - Try agin later

while (True):
    inp= int(input("Enter the numbre :"))
    if inp>100:
        print("congrats you entered the number greater than 100\n")
        break
    else:
        print("Try again later")
        continue