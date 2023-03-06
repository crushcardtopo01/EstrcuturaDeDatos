from Dog import Dog
from stack import *

dog1 = Dog("nombre","color",2,"electric",3)
dog2 = Dog("nombre","color",2,"electric",3)
dog3 = Dog("nombre3","color",2,"electric",3)
dog4 = Dog("nombre","color",2,"electric",3)

list1 = [dog1,dog2]

AddElement(list1,dog3)
ShowStack(list1)