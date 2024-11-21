#Writing a simple calculator program

#Ask the user for numerical input
num1= float (input("Enter the first number: "))
num2= float (input("Enter the second number: "))

#Operator input
operator = input("Enter an operator: +,-,/,*:")

if operator == "+": 
    result = num1 + num2
    print (f"{num1} + {num2} = {result}")
elif operator == "-" :
    result = num1 - num2
    print((f"{num1} - {num2} = {result}"))
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/" :
    if num2 !=0:
        result = num1/num2
        print (f"{num1} / {num2} = {result}")
    else: 
        print("Error, zero is not allowed")
else:
    print ("Invalid operator. Please enter +,-,*, or /")