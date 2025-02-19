#list data structures
#its ordered,mutable and has index

cars=["lamborghini","bugatti","ferrari","porsche","mustang'"]
print(cars)
cars[3]="Tesla"
print(f"i love driving {cars[3]}")
numbers=[1,4,6,9,3,10,12,4,6]
numbers.sort()
numbers.append("Ford")
print(numbers[3])
numbers.pop(3)
numbers.reverse()
print(numbers)

#turple data structure
#its ordered
#its immutable(cant change the value of sth)

fruits=("apples","banana","orange","strawberry")
number=(10,2,9,17,3,5,6,7,8)
print(fruits)
print(sorted(number))
cars.reverse()
print(f"I love eating {fruits[0]}")

# set data structure

cities={"Nairobi","Washington DC","Texas","New York","Oklahoma","Los Vegas"}
print(cities)
cities.pop()
print(cities)

# dictionary data structure

student={"Name":"Stacy","Gender":"Female","Age":"17","Phone Number":"718789441"}
print(f"My name is {student['Name']} and I am {student['Age']} years old." f"My gender is {student['Gender']} and my phone number is {student['Phone Number']}.")

