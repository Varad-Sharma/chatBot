import sys
import time
import wikipedia

isRunning = True


def askWiki(string):
    print(wikipedia.summary(string))


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
        

    elif qurie == "Bye":
        print("Bye\nSee You next time")
        time.sleep(1.5)
        sys.exit()
        isRunning = False
    
    else:
        print("I can answer only limited questions\n It is a prototye version")
        print("Or type again in first word capital\n")
    
