print("Welcome to the Rule based chatbot")
print("You can ask me basic questions and type 'bye' to exit the chat")

# Chatbot memory creation
responses = {
    "hello" : "Welcome! How may I help you?",
    "how are you" : "I'm Fine. Thank you for asking!",
    "who are you" : "I'm a smart AI chatbot",
    "motivate me" : "Manzil ko bhulakar jiya toh kya jiya",
    "happy" : "Great to hear that"
    }
# Making function to get reply

def getresponse(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
        return "Sorry I didn't understand you"

    return "Program execution end"

# Take user input
while True:
    userinput = input("Please ask your question: ")
    reply = getresponse(userinput)
    print(reply)

    if reply.lower() == "bye":
        break
    else:
        continue