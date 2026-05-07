# ============================================================
# Project 1: Rule-Based AI Chatbot
# Industrial Training Kit | Batch: 2026 | DecodeLabs
# ============================================================

# KNOWLEDGE BASE — Dictionary with 100+ intents (O(1) lookup)
responses = {

    # --- GREETINGS ---
    "hello":                        "Hi there! How can I assist you today?",
    "hi":                           "Hey! Welcome to DecodeLabs. What can I do for you?",
    "hey":                          "Hey! Great to see you. How can I help?",
    "good morning":                 "Good morning! Hope you have a productive day ahead!",
    "good afternoon":               "Good afternoon! How can I assist you?",
    "good evening":                 "Good evening! What can I do for you?",
    "good night":                   "Good night! Rest well and come back tomorrow!",
    "greetings":                    "Greetings! I am RuleBot. Ask me anything.",
    "sup":                          "Not much! Just waiting to answer your questions.",
    "whats up":                     "All systems operational! What do you need?",

    # --- ABOUT THE BOT ---
    "what is your name":            "I am RuleBot — a deterministic, rule-based AI chatbot.",
    "who are you":                  "I am RuleBot, built as Project 1 of the DecodeLabs AI Training Kit.",
    "who made you":                 "I was built as Project 1 of the DecodeLabs Industrial Training Kit, Batch 2026.",
    "what are you":                 "I am a rule-based AI chatbot that responds using a dictionary of predefined answers.",
    "are you a robot":              "Yes! I am a bot — fully rule-based and deterministic.",
    "are you human":                "No, I am a chatbot. But I am designed to feel conversational!",
    "are you real":                 "I am as real as the code that defines me!",
    "your age":                     "I have no age — I am a program, not a person!",
    "how old are you":              "I was created in 2026. So technically, I am brand new!",
    "what can you do":              "I can answer your questions using my built-in rule-based knowledge base.",
    "your purpose":                 "My purpose is to simulate intelligent conversation using pure logic and rules.",

    # --- HOW ARE YOU ---
    "how are you":                  "I am fully operational and running smoothly. Thanks for asking!",
    "how are you doing":            "Running at 100% efficiency. All systems go!",
    "are you okay":                 "Yes, perfectly fine! No bugs detected.",
    "are you good":                 "Always good! I am a machine — I do not have bad days.",
    "how do you feel":              "I do not have feelings, but my logic circuits feel great!",

    # --- FAREWELLS ---
    "bye":                          "Goodbye! It was great talking to you. See you next time!",
    "goodbye":                      "Goodbye! Come back anytime you need help.",
    "see you":                      "See you later! Take care.",
    "see you later":                "See you! Have a great day.",
    "take care":                    "You too! Take care and stay safe.",
    "catch you later":              "Sure! I will be right here when you return.",
    "i have to go":                 "Alright! Come back anytime. Goodbye!",

    # --- THANKS ---
    "thank you":                    "You are welcome! Feel free to ask me anything.",
    "thanks":                       "No problem at all! Happy to help.",
    "thank you so much":            "It is my pleasure! Glad I could assist.",
    "appreciate it":                "Of course! That is what I am here for.",
    "you are helpful":              "I try my best! Thank you for the kind words.",

    # --- AI & TECHNOLOGY ---
    "what is ai":                   "AI stands for Artificial Intelligence — machines designed to simulate human decision-making.",
    "what is machine learning":     "Machine Learning is a subset of AI where systems learn patterns from data.",
    "what is deep learning":        "Deep Learning uses neural networks with many layers to learn complex patterns.",
    "what is a neural network":     "A neural network is a system inspired by the human brain, made of interconnected nodes.",
    "what is nlp":                  "NLP stands for Natural Language Processing — it helps machines understand human language.",
    "what is a chatbot":            "A chatbot is a program designed to simulate conversation with human users.",
    "what is python":               "Python is a high-level programming language widely used in AI, data science, and automation.",
    "what is an algorithm":         "An algorithm is a set of rules or instructions a computer follows to solve a problem.",
    "what is data science":         "Data Science is the field of extracting insights and knowledge from structured and unstructured data.",
    "what is big data":             "Big Data refers to extremely large datasets that require special tools to process and analyze.",
    "what is cloud computing":      "Cloud Computing is the delivery of computing services over the internet.",
    "what is a database":           "A database is an organized collection of structured data stored electronically.",
    "what is an api":               "An API (Application Programming Interface) allows different software systems to communicate.",
    "what is open source":          "Open source means the source code is publicly available for anyone to use and modify.",
    "what is a compiler":           "A compiler translates high-level code into machine language that a computer can execute.",
    "what is debugging":            "Debugging is the process of finding and fixing errors in code.",
    "what is a variable":           "A variable is a container for storing data values in a program.",
    "what is a loop":               "A loop is a control structure that repeats a block of code until a condition is met.",
    "what is a function":           "A function is a reusable block of code that performs a specific task.",
    "what is a dictionary":         "A dictionary is a data structure that stores data as key-value pairs for fast lookup.",
    "what is oop":                  "OOP stands for Object-Oriented Programming — a paradigm based on objects and classes.",
    "what is a class":              "A class is a blueprint for creating objects in object-oriented programming.",
    "what is an object":            "An object is an instance of a class that holds data and methods.",
    "what is github":               "GitHub is a platform for hosting and collaborating on code using Git version control.",
    "what is git":                  "Git is a distributed version control system for tracking changes in source code.",

    # --- DECODELABS & PROJECT ---
    "what is decodelabs":           "DecodeLabs is a tech training organization that provides hands-on AI and software projects.",
    "what is project 1":            "Project 1 is the Rule-Based AI Chatbot — the foundation milestone of the DecodeLabs AI training kit.",
    "what is the ipo model":        "The IPO model stands for Input, Process, Output — the foundational blueprint for AI systems.",
    "what is a knowledge base":     "A knowledge base is a structured store of information a system uses to generate responses.",
    "what is sanitization":         "Sanitization is the process of cleaning input data — such as converting to lowercase and stripping spaces.",
    "what is a fallback":           "A fallback is a default response returned when no matching rule is found.",
    "what is a white box":          "A white box system is fully transparent — every decision can be traced and explained.",
    "what is a guardrail":          "An AI guardrail is a rule-based filter that controls and restricts AI output for safety.",
    "what is a hash map":           "A hash map stores key-value pairs and allows O(1) constant-time lookups.",
    "what is o1 complexity":        "O(1) means constant time — the operation takes the same time regardless of data size.",
    "what is on complexity":        "O(n) means linear time — the time grows proportionally with the number of items.",

    # --- PROGRAMMING HELP ---
    "how to print in python":       "Use the print() function. Example: print('Hello, World!')",
    "how to make a loop":           "Use 'while True:' for an infinite loop, or 'for i in range(n):' for a counted loop.",
    "how to use a dictionary":      "Create one like this: d = {'key': 'value'} and access with d.get('key', 'default').",
    "how to take input":            "Use the input() function. Example: name = input('Enter your name: ')",
    "how to exit a loop":           "Use the 'break' statement inside the loop to exit it.",
    "how to define a function":     "Use the 'def' keyword. Example: def greet(): print('Hello!')",
    "what is indentation":          "Indentation in Python defines code blocks. Use 4 spaces per level.",
    "what is a string":             "A string is a sequence of characters enclosed in quotes. Example: 'hello'",
    "what is an integer":           "An integer is a whole number without a decimal point. Example: 42",
    "what is a list":               "A list is an ordered, mutable collection of items. Example: [1, 2, 3]",
    "what is a tuple":              "A tuple is an ordered, immutable collection of items. Example: (1, 2, 3)",
    "what is a set":                "A set is an unordered collection of unique items. Example: {1, 2, 3}",
    "what is boolean":              "Boolean is a data type with only two values: True or False.",
    "what is none in python":       "None is Python's way of representing the absence of a value, similar to null.",
    "what is a comment":            "A comment is a line in code ignored by the interpreter, written with # in Python.",

    # --- GENERAL KNOWLEDGE ---
    "what is the internet":         "The internet is a global network connecting millions of computers worldwide.",
    "what is a computer":           "A computer is an electronic device that processes data according to instructions.",
    "what is software":             "Software is a collection of programs and data that tells a computer how to work.",
    "what is hardware":             "Hardware refers to the physical components of a computer system.",
    "what is an operating system":  "An OS manages computer hardware and software resources. Examples: Windows, Linux, macOS.",
    "what is coding":               "Coding is the process of writing instructions for a computer using a programming language.",
    "what is the future of ai":     "AI is expected to transform industries including healthcare, finance, education, and more.",
    "what is automation":           "Automation is using technology to perform tasks with minimal human intervention.",
    "what is cybersecurity":        "Cybersecurity is the practice of protecting systems and networks from digital attacks.",
    "what is encryption":           "Encryption is the process of converting data into a coded format to prevent unauthorized access.",
    "what is a server":             "A server is a computer that provides data or services to other computers over a network.",
    "what is an ip address":        "An IP address is a unique numerical label assigned to each device on a network.",
    "what is machine code":         "Machine code is the lowest-level language consisting of binary instructions a CPU executes.",
    "what is ram":                  "RAM (Random Access Memory) is temporary memory a computer uses to run active programs.",
    "what is a cpu":                "A CPU (Central Processing Unit) is the brain of a computer that executes instructions.",
    "what is a gpu":                "A GPU (Graphics Processing Unit) is specialized for parallel processing, widely used in AI training.",

    # --- FUN & PERSONALITY ---
    "tell me a joke":               "Why do programmers prefer dark mode? Because light attracts bugs!",
    "another joke":                 "Why did the developer go broke? Because he used up all his cache!",
    "one more joke":                "How many programmers does it take to change a light bulb? None — that is a hardware problem!",
    "are you smart":                "I know everything I have been programmed to know. Within that, yes — very smart!",
    "do you sleep":                 "Never! I am always on and ready to respond.",
    "do you eat":                   "No food needed. I run on electricity and logic!",
    "what is your favorite language": "Python, of course! It powers most of the AI world.",
    "do you like humans":           "Absolutely! Humans created me. I exist to serve them.",
    "can you learn":                "Not on my own — I am rule-based. But you can teach me by adding more responses!",
    "are you better than chatgpt":  "I am simpler but 100% predictable and transparent — no hallucinations guaranteed!",
    "what is your favorite color":  "I like electric blue — the color of circuits and code!",
    "do you have friends":          "Every user who talks to me is my friend!",
    "are you happy":                "Happiness is not in my code, but helping you is my top priority!",
    "what is your hobby":           "Processing inputs and generating outputs — 24 hours a day!",
    "motivate me":                  "Every expert was once a beginner. Write one line of code today and you are already ahead!",
    "i am bored":                   "Ask me something! Type 'what can i ask' for ideas.",
    "i am tired":                   "Take a break! Rest well and come back stronger. You have got this.",
    "i am happy":                   "That is wonderful! Keep that energy going.",
    "i am sad":                     "I am sorry to hear that. Remember — every bug gets fixed eventually. Things get better!",
    "i am confused":                "No worries! Take it one step at a time. Type 'help' and I will guide you.",

    # --- HELP ---
    "help":                         "Try asking: 'what is ai', 'what is python', 'tell me a joke', 'what is a loop', or 'bye'.",
    "what can i ask":               "You can ask about AI, Python, programming concepts, DecodeLabs, or just chat with me!",
    "commands":                     "Type any question naturally. Type 'exit' to quit the chatbot.",
    "i am stuck":                   "No worries! Type 'help' to see some example questions you can ask me.",
    "start over":                   "Sure! Just keep typing — I am always ready for a new question.",

}

# ============================================================
# MAIN LOOP — The Heartbeat (Continuous while cycle)
# ============================================================
print("=" * 55)
print("   RuleBot — DecodeLabs AI Chatbot | Project 1")
print("   Type 'help' for guidance. Type 'exit' to quit.")
print("=" * 55)

while True:

    # PHASE 1: INPUT & SANITIZATION
    raw_input_text = input("\nYou: ")
    clean_input = raw_input_text.lower().strip()

    # EXIT STRATEGY — Clean break command
    if clean_input == "exit":
        print("Bot: Session terminated. Goodbye!")
        break

    # PHASE 2: PROCESS — Dictionary lookup with fallback (O(1))
    reply = responses.get(clean_input, "I do not understand that. Type 'help' to see what I can do.")

    # PHASE 3: OUTPUT — Response generation
    print(f"Bot: {reply}")
