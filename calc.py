print("Kalkulator")
choice = input("Enter the operator (* / - +) : ")
num1 = float(input("First number : "))
num2 = float(input("Second number : "))
#operator choice
if choice == '*': 
    print(num1 * num2)
elif choice == '/':
    print(num1 / num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '+':
    print(num1 + num2)
else:
    print("invalid operator")