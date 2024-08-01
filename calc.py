# Simple Calculator

print("select an opration to perform")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation=input()

if operation == "1":
    num1=int(input())
    num2=int(input())
    print(num1 + num2)
elif operation == "2":
    num1=int(input())
    num2=int(input())
    print(num1 - num2)
elif operation == "3":
    num1=int(input())
    num2=int(input())
    print(num1 * num2)
elif operation == "4":
    num1=int(input())
    num2=int(input())
    print(num1 / num2)
else:
    print ("invalid entry")
    