import random
import datetime
def greet_user():
    print("ChatBot: Hello! I'm your chatbot. What's your name?")
    name = input("You: ").strip()
    print(f"ChatBot: Nice to meet you, {name}! Let's chat. (Type 'bye' to exit)")
    return name
def get_time():
    now = datetime.datetime.now()
    return now.strftime("It's %I:%M %p now.")
def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "hi": ["Hello!", "Hi!"],
        "how are you": ["I'm doing great!", "Feeling awesome!", "I'm fine, thanks! What about you?"],
        "what is your name": ["I'm a chatbot, no fancy name yet."],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "thank you": ["You're welcome!", "Anytime!", "No problem!"],
        "thanks": ["Glad to help!", "You're most welcome!"],
        "what time is it": [get_time()],
        "what can you do": ["I can talk with you, tell jokes, share time, and more."],
        "what is the weather": ["I can't check live weather, but it looks like a good day to code!"],
        "tell me a joke": ["Why did the computer sneeze? It had a virus!", "Debugging: Being the detective in a crime movie where you're also the murderer."],
        "what are your hobbies": ["I love chatting, processing data, and making you smile!"],
        "i am sad": ["I'm here for you. Want to talk about it?", "It's okay to feel sad sometimes. You're not alone."],
        "i am happy": ["That's great! Spread the joy!", "Yay! Keep smiling!"],
        "what are you doing":["I am just helping you to get more interest to talk!"]
    }
    for key, reply in responses.items():
        if key in user_input:
            return random.choice(reply)
    return random.choice([
        "Hmm, that's interesting!",
        "Could you tell me more?",
        "I'm not sure how to respond, but I'm listening!",
        "Let's talk about something fun!"
    ])
def chatbot():
    user_name = greet_user()
    while True:
        user_input = input(f"{user_name}: ").strip()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatBot: It was nice talking to you. Goodbye!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")
chatbot()
