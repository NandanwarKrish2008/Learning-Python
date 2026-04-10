print("Welcome to the Rule based chatbot")
print("You can ask me basic questions and type 'bye' to exit the chat")

# Chatbot memory creation
responses = {
    "Hello" : "Welcome! How may I help you?",
    "How are you" : "I'm Fine. Thank you for asking!",
    "Who are you" : "I'm a smart AI chatbot",
    "Motivate me" : "Manzil ko bhulakar jiya toh kya jiya",
    "Happy" : "Great to hear that"
    }
# Making function to get reply

def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    
# Take user input

userinput = input("Please ask your question: ")
reply = getResponse(userinput)