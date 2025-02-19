
class Dad:
    def __init__(self, height,dad_hobby,):
        self.height = height
        self.dad_hobby =dad_hobby

class Mum:
    def __init__(self, height,mum_hobby,):
        self.height = height
        self.mum_hobby = mum_hobby
class Boy(Dad):
    def boy_inherits(self):
        print(f"The boy inherits {self.dad_hobby} and a height of {self.height} from his father")

my_object=Boy(height='6.3', dad_hobby='playing chess')
my_object.boy_inherits()

class Girl(Mum):
    def girl_inherits(self):
        print(f"The girl inherits {self.mum_hobby} and a height of {self.height} from her mother")

my_object=Girl(height='5.5', mum_hobby='reading novels')
my_object.girl_inherits()

