# program that determines a leap year

year = int(input("Enter a year: "))
if year % 4 == 0:
            print(f"The year {year} is a leap year.")
else:
        print(f"The year {year} is not a leap year.")