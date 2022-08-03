print("I am a Student  advisor chat bot")
elif 'what is your name'in a:
        x= input()
        print("thank you "+x)
        print(" I am here to explore you about the core courses required for the specialization's offered in K L University. CSE Department ")
elif 'what are the specializations  will be provided'in a:
        print("Here are the specialization's offered by K L University CSE Department:")
        print("1. Software Modelling & Devops\n2. Internet of Things\n3. Cloud & Edge Computing\n4. Graphics, Gaming & UX Design")
        print("5. Cyber Security & Blockchain Technology\n6. Artificial Intelligence & Intelligence Process Automatio\n7. Data Science & Big Data Analytics\n8.Computer Communications\n9. Exit")
elif 'what Spciliasation Would you like to choose' in a:
        x=input()
        print("The specialisation"+x+"is good")
        print("Global Certification': 'PCAP Certified associate in Python Programming certiification'. 'Core Cour")
elif 'How are you' in a:
        print("I am fine")
elif 'are you working?' in a:
        print("yes. I'am working in KLuniversity as a Professor")
elif 'what is your name?' in a:
        print("My name is", b)
elif 'ok' in a:
        print("Nice name and Nice meeting you")
elif 'what did you do yesterday?' in a:
        print("I have done Coding challenge in codechef")
elif 'bye' in a:
        print("Ok bye, Meet you later, Have a good day")
else:
        print("I can't able to understand your question")


name1 = input("Enter your friend you would like to chat : ")
print("You may ask any one of these questions")
print("Hi")
print("What is your name:")
print("what are the specializations  will be provided")
print("What Specialisation would like to choose")
print("How are you?")
print("Are you working?")
print("what is your name?")
print("what did you do yesterday?")
while True:
    message = input("Type a message here : ")
    if (message == 'bye'):
        print("Ok bye,meet you later!")
        break
    else:
        chatbox(message, name1)