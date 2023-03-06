from Animal import Animal

class Dog(Animal):

    def __init__(self,name:str,color:str,eye:int,breed:str,age:int):
        super().__init__(name,color,eye)
        self.breed = breed
        self.age = age
        self.is_set = False
    
    def __str__(self):
        info = super().__str__()+"breed: "+self.breed+" age: "+str(self.age)
        return info
    
    
    
    def get_breed(self):
        return self.breed
    
    def make_sound():
        return "guau!"
    
    def get_sit(self):
        return self.is_set
    
    def sit(self):
        self.is_set = True
    def up (self):
        self.is_set = False