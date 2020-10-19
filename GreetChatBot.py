import datetime
import random
import webbrowser

def greeting():
    responses = [
        "Welcome, I am a  chatbot. I hope i will be useful to  you, Your name please : ",
        "Hey hello! I am your chatbot I can help you. May I know your name? : "
    ]
    print(random.choice(responses))
def wishday(name):
    time_now = datetime.datetime.now().hour
    if time_now < 12:
        print("Nice to meet you " + name + ", Good morning.")
    elif time_now > 12 and time_now < 17:
        print("Nice to meet you " + name + ", Good afternoon.")
    elif time_now > 18 and time_now <22:
        print("Nice to meet you " + name + ", Good evening.")
    else:
        print("I think it's a little bit late " + name + ".")
def menu():
    print("1 : I want to listen some music")   
    print("2 : I want to shop")
    print("3 : End the conversation")
    choice = 0
    while (choice != 3):
        try:
            choice = int(input("Choose your choice"))
        except:
            print("Invalid input")
            continue
        if choice == 1:
            webbrowser.open("https://gaana.com/", new = 1)
        elif choice == 2:
            webbrowser.open("https://www.amazon.in/", new = 1)
        else:
            print("Invalid input")
def bot():
    greeting()
    try:
      name = input()
    except:
      print("Enter a Valid Name")
      greeting()
    wishday(name)
    menu()
bot()
