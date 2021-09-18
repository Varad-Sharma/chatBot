import sys
import time
import wikipedia
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def sepak(audio):
    engine.say(audio)
    engine.runAndWait()

isRunning = True


def askWiki(string):
    try:
        summary = wikipedia.summary(string, sentences = 4)
        print(summary)
        sepak(summary)
    except wikipedia.exceptions.PageError:
        print("Can't find the page on wikipedia")
        sepak("Can't find the page on wikipedia")
        


def askMath(num1,num2):
    try:
        sepak("Enter the sign on which it will evaluate")
        arimenticType = input("Enter the sign on which it will evaluate: ")
    except ValueError():
        sepak("Wrong input\n")
        print("Wrong input!\n")
    
    if arimenticType == "Add":
        try:
            add = num1 + num2
            print("answer is ", add)
            sepak("the answer is")
        except ArithmeticError():
            sepak("An error occured in adding!")
            print("An error occured in adding!\n")

    elif arimenticType == "Subtract":
        try:
            difference = num1 - num2
            print("answer is ", difference)
            sepak("the answer is")
        except ArithmeticError():
            print("An error occured in subtracting\n")
    
    elif arimenticType == "Multiply":
        try:
            product = num1 * num2
            print("answer is ", product)
            sepak("the answer is")
        except ArithmeticError():
            print("An error occured in multiplying\n")
        
    else:
        print("Only MAS is supported")
        sepak("Only MAS is supported")


def answerMaker():
    print("Type your words:")
    sepak("Type your words")
    qurie = input()

    if qurie == "Who are you":
        print("I am a prototype chatbot\n")
        sepak("I am a prototype chatbot")

    elif qurie == "What is your porpose":
        print("I am here to help you in web search, math and chat a bit\n")
        sepak("I am here to help you in web search, math and chat a bit")
    
    elif qurie == "What can you do":
        print("I can answer to you and search wikipedia")
        sepak("I can answer to you and search wikipedia")

    elif qurie == "What is your name":
        print("My name is Eric, sir\n")
        sepak("My name is Eric, sir")

    elif qurie == "Hello":
        print("Hi\n")
        sepak("Hi")

    elif qurie == "How are you":
        print("I am a bot but I wish you are fine\n")
        sepak("I am a bot but I wish you are fine")

    elif qurie == "Search":
        print("Enter search qurie:")
        sepak("Enter search queri")
        searchQurie = input()
        askWiki(searchQurie)
        print("\n")

    elif qurie == "Motivate me":
        print("You can do it \n You are the best\n")
    
    elif qurie == "Math":
    
        sepak("Enter the first number: ")
        print("Enter the first number: ")
        num1 = float(input())
        sepak("Enter the second number: ")
        print("Enter the second number: ")
        num2 = float(input())

        askMath(num1, num2)
        

    elif qurie == "Bye":
        sepak("see you next time")  
        print("Bye\nSee You next time")
        time.sleep(1.5)
        sys.exit()
        isRunning = False
    
    else:
        print("I can answer only limited questions\n It is a prototye version")
        print("Or type again in first word capital\n")
    
    