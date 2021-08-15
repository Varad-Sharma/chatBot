import sys
import time
import wikipedia

isRunning = True


def askWiki(string):
    try:
        print(wikipedia.summary(string))
    except wikipedia.exceptions.PageError:
        print("Can't find the page")


def askMath(num1,num2):
    try:
        arimenticType = input("Enter the sign on which it will evaluate: ")
    except ValueError():
        print("Wrong input!\n")
    
    if arimenticType == "Add":
        try:
            add = num1 + num2
            print("answer is ", add)
        except ArithmeticError():
            print("An error occured in adding!\n")

    elif arimenticType == "Subtract":
        try:
            difference = num1 - num2
            print("answer is ", difference)
        except ArithmeticError():
            print("An error occured in subtracting\n")
    
    elif arimenticType == "Multiply":
        try:
            product = num1 * num2
            print("answer is ", product)
        except ArithmeticError():
            print("An error occured in multiplying\n")
        
    else:
        print("Only MAS is supported")


def answerMaker():
    print("Type your words:")
    qurie = input()

    if qurie == "Who are you":
        print("I am a prototype chatbot\n")

    elif qurie == "What is your porpose":
        print("I am here to help you in web search and chat a bit\n")
    
    elif qurie == "What can you do":
        print("I can answer to you and sear wikipedia")

    elif qurie == "What is your name":
        print("My name is Eric, sir\n")

    elif qurie == "Hello":
        print("Hi\n")

    elif qurie == "How are you":
        print("I am a bot but I wish you are fine\n")

    elif qurie == "Search":
        print("Enter search qurie:")
        searchQurie = input()
        askWiki(searchQurie)
        print("\n")

    elif qurie == "Motivate me":
        print("You can do it \n You are the best\n")
    
    elif qurie == "Math":
    
        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())
    
        print("Wrong input\n")

        askMath(num1, num2)
        

    elif qurie == "Bye":
        print("Bye\nSee You next time")
        time.sleep(1.5)
        sys.exit()
        isRunning = False
    
    else:
        print("I can answer only limited questions\n It is a prototye version")
        print("Or type again in first word capital\n")
    
