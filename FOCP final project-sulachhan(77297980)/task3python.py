from random import choice
random_string=lambda lst:choice(lst)
name_from_email=lambda email:email.split("@")[0]
inword=lambda sent,word : True if word.lower() in sent.lower() else False
isemail = lambda email,domain: False if (email.count("@")!=1 or len(email.split("@")[0])<2 or email.split("@")[1]!=domain) else True
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")

email=input("Please enter your Poppleton email address:")
options={        
    "library":"The library is closed today.",
    "WiFi":"WiFi is excellent across the campus.",
    "deadline":"Your deadline has been extended by two working days.",
    "books":"The library will be open tomorrow at 6",
    "teacher":"The teacher's lounge is in the 7th floor",
    "lab":"The lab is closed today.",
    "network_error":[False,False,False,False,False,False,False,False,False,True],
    "operator_names":["Kevin","Louis"],
    "words":["bye","exit","help"],
    "no_comebacks":["sorry,come again","I did'nt get you","hmm","I see"]
    }

if(isemail(email,"pop.ac.uk")):
    print(f"Hi, {name_from_email(email)}! Thank you, and Welcome to PopChat!")
    print(f'My name is {random_string(options["operator_names"])}, and it will be my pleasure to help you.')

    while True:
        no_output=True
        sent=input("-->")

        if random_string(options["network_error"]):
            print("Network error")
            break

        if any(inword(word , sent) for word in options["words"]):
            print("Thanks, {}, for using PopChat. See you again soon!".format(name_from_email(email)))

            break

        for key in set(options)-set(["network_error","operator_names","words"]):
            if inword(sent,key):
                print(options[key])
                no_output=False
        if no_output==True:
                print(random_string(options["no_comebacks"]))    
else:
    print("This email is not valid")