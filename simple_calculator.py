num=float(input("Enter the first number: "))
num1=float(input("Enter the second number: "))
operator=input("Enter the operator(+,_,*,/): ")

if operator=="+":
    result=num+num1
    print(f"The result of {num} {operator} {num1} is {result}")

elif operator == "-"  :
    result=num-num1
    print(f"The result of {num} {operator} {num1} is {result}")

elif operator=="*":
    result=num*num1
    print(f"The result of {num} {operator} {num1} is {result}")

elif operator=="/":
    if num1 != 0:
        result=num/num1
        print(f"The result of {num} {operator} {num1} is {result}")
    else:
        print(f"Cannot be divided by 0")
else:
    print("Invalid operator")