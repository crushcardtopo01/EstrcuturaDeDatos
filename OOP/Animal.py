class Animal:
    def __init__(self,name:str,color:str,eye:int):
        self.name = name
        self.color = color
        self.eye = eye
        self.is_alive = True
        self.is_move = False
    
    def __str__(self):
        text = "name: "+self.name+" color: "+self.color+" eye: "+str(self.eye) + " is alive: "+str(self.is_alive)+" is move: "+str(self.is_move)
        return text
    
    def get_alive(self):
        return self.is_alive
    
    def set_alive(self,is_alive:bool):
        self.is_alive = is_alive

    def set_move(self,move):
        self.is_move = move
    
    def get_move(self):
        return self.is_move
    
    def make_sound():
        return "animal sound"
