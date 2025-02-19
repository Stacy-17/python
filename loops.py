# while loop
num=1
while num<=7:
    print(num)
    num+=1

num2=5                                                    
while num2<=70:
    print(num2)
    num2+=10

    # for loop

for num1 in range(1,11):
    print(num1)

fruits=['apple','grapes','blueberries']

for i in fruits:
    print(i)

name="Stacy"

for n in name:
    print(n)

numbers=[1,-4,3,-6,5,-7,8,3,8,-4,14,24,40,12,-20]

sum_even=0

for num in numbers:
    if num % 2 == 0:
        sum_even+=num
print(f"The sum of even numbers is {sum_even}")

