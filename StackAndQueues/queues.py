

def RemoveElement(queue):
    _queue = queue
    if(len(_queue) != 0):
        #if you dont define a index, pop method remove the last item inside of the list
        _queue.pop(0)
    else:
        print("\n \nThe queue dont have elements!!")
    return _queue

def AddElement(queue):
    _queue = queue
    newElement = input(" \n \nEnter the new element: ")
    _queue.append(newElement)
    return _queue

def ShowQueue(queue):
    print("XXXXXXXXXX   Queue    XXXXXXXXXXXX")
    print(queue)
    print("XXXXXXXXXXXXXXXXXXXXXX\n\n")

def Queue():
    queue = []
    print("\n \n\n \nWelcome to Queues!! ")
    isActive = True
    while(isActive):
        print("Choose a option")
        print("1.- add element")
        print ("2.- remove element")
        print("3.- see the queue")
        print("4.- exit")
        option = input("enter you option: ")
        
        if(option =="1"):
            queue = AddElement(queue)
        if(option =="2"):
            queue = RemoveElement(queue)
        if(option =="3"):
            ShowQueue(queue)
        if(option =="4"):
            isActive = False