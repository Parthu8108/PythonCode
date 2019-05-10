class parthuu:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def funct(self):
        print("The name is "+self.name)

p_object=parthuu("Parthuu",21)
print(p_object.name)
print(p_object.age)
p_object.funct()
