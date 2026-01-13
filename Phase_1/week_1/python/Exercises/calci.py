a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

symbol=input("Enter operation (+, -, *, /): ")
if symbol=="+":
    print(f"Addition of {a}+{b} is {a+b}")
          
elif symbol=="-":
    print(f"Subtraction of {a}-{b} is {a-b}")
elif symbol=="*":
    print(f"Multiplication of {a}*{b} is {a*b}") 

elif symbol=="/":
    if b!=0:
        print(f"Division of {a}/{b} is {a/b}")
    else:
        print("Error: Division by zero is not allowed.")                            