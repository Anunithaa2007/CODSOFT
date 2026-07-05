#CODSOFT AI Internship-Task 1
print("=" * 50)
print("🤖 Welcome to the Smart Rule-Based AI Chatbot")
print("=" * 50)
print("Hello! I am your Smart AI Chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' anytime to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hi" or user == "hello":
        print("Bot: Hello Friend! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is AtomBot😊.")

    elif user == "how you are created":
        print("Bot: I was created using Python as a rule-based chatbot.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "help":
        print("Bot: You can ask about my name, creator, Python, AI, or greet me.")

    elif user == "python":
        print("Bot: Python is one of the most popular programming language used for AI, web development, and data science.")

    elif user == "artificial intelligence" or user == "ai":
        print("Bot: Artificial Intelligence enables machines to learn, reason, and solve problems.")

    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome! I'm always happy to help.😊")

    elif user == "good morning":
        print("Bot: Good morning! Have a wonderful day ahead.")

    elif user == "good afternoon":
        print("Bot: Good afternoon! Hope you're having a great day.")

    elif user == "good evening":
        print("Bot: Good evening! How can I assist you?")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day. 😊")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")