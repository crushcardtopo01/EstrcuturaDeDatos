import  queues


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
            print("something")
        if (option == "3"):
            isActive = False

    print("good bye! 🙃 ")

__main__()