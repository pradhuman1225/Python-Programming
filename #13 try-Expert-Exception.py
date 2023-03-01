print("Enter the num1 :")
num1= input()
print("Enter the num2 :")
num2= input()

# try to handle user input wrong value.

try:
    print("The sum of two number is ",
     int(num1)+int(num2))

except Exception as e:
    print(e)

print("This line is very important")
