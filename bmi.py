# create a program that calculates you bmi

weight=float(input("Enter weight in kilograms: "))
height=float(input("Enter height in meters: "))
bmi:float=weight/(height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and is classified as underweight.")
elif 18.5 <= bmi <= 24.9:
    print(f"Your BMI is {bmi} and is classified as normal.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi} and is classified as overweight.")
else:
    print(f"Your BMI is {bmi} and is classified as obese.")



