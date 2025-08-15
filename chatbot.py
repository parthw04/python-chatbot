# =============================== Task 8 - Chat-Bot ====================

import random

small_talk_responses = [
    "Did you know? Honey never spoils! Archaeologists found 3000-year-old honey that's still edible. 🍯",
    "Here’s a fun one: Bananas are berries, but strawberries aren’t! 🍓",
    "Why don’t skeletons fight each other? Because they don’t have the guts! 💀",
    "Fun fact: Octopuses have three hearts. ❤️❤️❤️",
    "Here’s a joke: Why did the computer go to the doctor? Because it caught a virus! 🖥️",
    "Did you know? A day on Venus is longer than a year on Venus. 🌌",
]

print("🤖 Hey there! I'm your friendly chatbot. Type 'bye' anytime to end our chat.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Chatbot: It was lovely chatting with you. Take care! 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hey! 😊 How’s your day going?")
    
    elif "how are you" in user_input:
        print("Chatbot: I’m feeling as good as a chatbot can! What about you?")
    
    elif "your name" in user_input:
        print("Chatbot: You can call me PyBot. I’m here to make your day easier!")
    
    elif "help" in user_input or "doubt" in user_input:
        print("Chatbot: Sure! You can ask me about my name, how I’m doing, or just say hi!")
    
    elif "good" in user_input or "fine" in user_input:
        print("Chatbot: That’s great to hear! 🌟")
    
    elif "bad" in user_input or "not good" in user_input:
        print("Chatbot: Oh no 😔. I hope things get better for you soon.")
    
    else:
        print("Chatbot:", random.choice(small_talk_responses))
