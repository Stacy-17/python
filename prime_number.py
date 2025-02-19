num1=int(input("Enter a number: "))

if num1<=1:
    is_Prime=False
elif num1==2:
    is_Prime=True
else:
    is_Prime=True
    for i in range(3,int(num1**0.5)+1,2):
        if num1 % i==0:
            is_Prime=False
            break
 if is_Prime:
     print(f"{num1} is a Prime number")
else:
     print(f"{num1} is not a Prime number")