
class cars:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def display(self):
        print(f"The make of the car is: {self.make},its model: {self.model},its year of manufacture: {self.year} and its color is : {self.color}")

my_object=cars("Ford","Mustang","2008","blue")
my_object.display()
my_object1 = cars("Toyota","Sienna","1997","black")
my_object1.display()
my_object2 = cars("Cybertruck","Tesla","2019","violet")
my_object2.display()
my_object3 = cars("Gla","Mercedes","2013","silver")
my_object3.display()
my_object4 = cars("Civic","Honda","1972","red")
my_object4.display()
my_object5 = cars("Leaf","Nissan","2010","white")
my_object5.display()