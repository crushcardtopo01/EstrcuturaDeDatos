import  queues
import stack


def __main__():
    isActive = True
    while(isActive):
        print("Welcome to my code!")
        print("Please choose a option")
        print("1.- Queues")
        print("2.- Stack")
        print("3.- exit")
        option = input(" Enter your option")

        if (option == "1"):
            queues.Queue()

        if (option == "2"):
            stack.Stack()
        if (option == "3"):
            isActive = False

    print("good bye! 🙃 ")

__main__()