

def RemoveElement(stack):
    _stack = stack
    if(len(_stack) != 0):
        _stack.pop(1)
    else:
        print("\n \nThe stack dont have elements!!")
    return _stack

def AddElement(stack,new_element):
    _stack = stack
    _stack.append(new_element)
    return _stack

def ShowStack(stack):
    print("XXXXXXXXXX   Stack    XXXXXXXXXXXX")
    for element in stack:
        print(element)
    print("XXXXXXXXXXXXXXXXXXXXXX\n\n")

def Stack():
    stack = []
    print("\n \n\n \nWelcome to Stack!! ")
    isActive = True
    while(isActive):
        print("Choose a option")
        print("1.- add element")
        print ("2.- remove element")
        print("3.- see the Stack")
        print("4.- exit")
        option = input("enter you option: ")
        
        if(option =="1"):
            stack = AddElement(stack)
        if(option =="2"):
            stack = RemoveElement(stack)
        if(option =="3"):
            ShowStack(stack)
        if(option =="4"):
            isActive = False