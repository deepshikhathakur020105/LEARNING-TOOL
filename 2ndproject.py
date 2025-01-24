import random
import os

print("""\
__        __   _                            _                 
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___           
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \          
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |         
__\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/          
|  _ \ _   _| |_| |__   ___  _ __                             
| |_) | | | | __| '_ \ / _ \| '_ \                            
|  __/| |_| | |_| | | | (_) | | | |                           
|_|    \__, |\__|_| |_|\___/|_| |_|                           
 ___   |___/                      _   _                       
|_ _|_ __ | |_ ___ _ __ __ _  ___| |_(_)_   _____             
 | || '_ \| __/ _ \ '__/ _` |/ __| __| \ \ / / _ \            
 | || | | | ||  __/ | | (_| | (__| |_| |\ V /  __/            
|___|_| |_|\__\___|_|  \__,_|\___|\__|_| \_/_\___|          _ 
| |    ___  __ _ _ __ _ __ (_)_ __   __ _  |_   _|__   ___ | |
| |   / _ \/ _` | '__| '_ \| | '_ \ / _` |   | |/ _ \ / _ \| |
| |__|  __/ (_| | |  | | | | | | | | (_| |   | | (_) | (_) | |
|_____\___|\__,_|_|  |_| |_|_|_| |_|\__, |   |_|\___/ \___/|_|
                                    |___/                     
""")


progress = {
    "topics_learned": [],
    "quiz_score": 0,
    "challenges_completed": 0
}

# Main menu
def main_menu():
    print("\n\033[38;2;255;0;255mPython Interactive Learning Tool!\033[0m")
    print("\033[1mSelect an option to continue:\033[0m")
    print("1. Learn Strings")
    print("2. Learn Loops")
    print("3. Learn Recursion")
    print("4. Learn Data Types")
    print("5. Learn File Handling")
    print("6. Learn Error Handling")
    print("7. Take a Quiz")
    print("8. Complete Challenges")
    print("9. View Created Files")
    print("10. View Help Menu")
    print("11. View Progress")
    print("12. Open Saved Code")
    print("13. Exit")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return 0

def learn_strings():
    print("\n\033[1mStrings in Python:\033[0m")
    print("\033[32mStrings are sequences of characters. Example:\033[0m")
    print('\033[32mmy_string = "Hello, World!"\033[0m')
    print("\033[32mCommon methods: upper(), lower(), replace(), split().\033[0m")
    progress["topics_learned"].append("Strings")

def learn_loops():
    print("\n\033[1m Loops in Python\033[0m ")
    print("\033[32mLoops are used for iterating over sequences or ranges.\033[0m")
    print("\033[32m1. For Loop: Iterates over a sequence (e.g., list, range).\033[0m")
    print("Example: \033[0m\033[32mfor i in range(5): print(i)\033[0m")
    print("\033[32m2. While Loop: Continues as long as a condition is true.\033[0m")
    print("Example: \033[0m\033[32mwhile x < 5: x += 1\033[0m")
    progress["topics_learned"].append("Loops")

def learn_recursion():
    print("\n\033[1m Recursion in Python\033[0m ")
    print("\033[32mRecursion is when a function calls itself.\033[0m")
    print("\033[32mCommon use cases: Factorials, Fibonacci sequence, Divide-and-conquer algorithms.\033[0m")
    progress["topics_learned"].append("Recursion")

def learn_data_types():
    print("\n\033[1m Data Types in Python\033[0m ")
    print("\033[32mPython supports various data types:\033[0m")
    print("\033[32m1. int: Integer numbers.\033[0m")
    print("\033[32m2. float: Decimal numbers.\033[0m")
    print("\033[32m3. str: Strings or text.\033[0m")
    print("\033[32m4. list: Ordered, mutable collections.\033[0m")
    print("\033[32m5. tuple: Ordered, immutable collections.\033[0m")
    print("\033[32m6. set: Unordered collections of unique elements.\033[0m")
    print("\033[32m7. dict: Key-value pairs.\033[0m")
    progress["topics_learned"].append("Data Types")

def learn_file_handling():
    print("\n\033[1m File Handling in Python\033[0m ")
    print("\033[32mPython makes it easy to work with files.\033[0m")
    print("\033[32mCommon modes:\033[0m")
    print("\033[32m1. 'r': Read\033[0m")
    print("\033[32m2. 'w': Write\033[0m")
    print("\033[32m3. 'a': Append\033[0m")
    print("\033[32mUse open() function. Example:\033[0m")
    print("\033[32mwith open('file.txt', 'r') as file:\033[0m")
    print("\033[32m    content = file.read()\033[0m")
    progress["topics_learned"].append("File Handling")

def learn_error_handling():
    print("\n\033[1m Error Handling in Python\033[0m ")
    print("\033[32mErrors are managed using try-except blocks.\033[0m")
    print("\033[32mExample:\033[0m")
    print("\033[32mtry:\033[0m")
    print("\033[32m    result = 10 / 0\033[0m")
    print("\033[32mexcept ZeroDivisionError as e:\033[0m")
    print("\033[32m    print('Error:', e)\033[0m")
    progress["topics_learned"].append("Error Handling")

# Quiz function
def quiz():
    questions = [
        ("\033[32mWhat is the output of 3 + 2 * 2?\033[0m", ["6", "7", "8", "9"], "7"),
        ("\033[32mWhich keyword is used to define a function in Python?\033[0m", ["func", "define", "def", "lambda"], "def"),
        ("\033[32mWhat method adds an item to a list?\033[0m", ["add", "append", "push", "insert"], "append"),
        ("\033[32mWhat does the 'break' statement do in a loop?\033[0m", ["Skips to the next iteration", "Stops the loop", "Restarts the loop", "Ends the program"], "Stops the loop"),
        ("\033[32mWhich data type is immutable?\033[0m", ["list", "dict", "tuple", "set"], "tuple"),
        ("\033[32mWhat does 'len()' function return?\033[0m", ["Length of a list", "Length of a tuple", "Length of a string", "All of the above"], "All of the above"),
        ("\033[32mWhat is the output of '5 // 2' in Python?\033[0m", ["2.5", "2", "3", "Error"], "2"),
        ("\033[32mWhich of these is a valid Python variable name?\033[0m", ["2var", "var_2", "@var", "var-2"], "var_2")
    ]
    question, options, correct = random.choice(questions)
    print("\n\033[1mPython Quiz\033[0m")
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    try:
        answer = int(input("Enter your choice: "))
        if options[answer - 1].lower() == correct.lower():
            print("Correct!")
            progress["quiz_score"] += 1
        else:
            print(f"Wrong. The correct answer is {correct}.")
    except (ValueError, IndexError):
        print("Invalid choice. Try again.")

# Challenges function
def challenges():
    print("\n\033[1mPython Challenges\033[0m")
    
    # List of challenge filenames
    challenge_files = [f"challenge_{i}.py" for i in range(1, 21)]
    
    # Dictionary mapping filenames to prompts
    challenge_prompts = {
        "challenge_1.py": "Write a function to check if a number is prime.",
        "challenge_2.py": "Write a function to reverse a string.",
        "challenge_3.py": "Write a function to find the largest element in a list.",
        "challenge_4.py": "Write a program to calculate the factorial of a number.",
        "challenge_5.py": "Write a program to find the nth Fibonacci number.",
        "challenge_6.py": "Write a function to sort a list of integers.",
        "challenge_7.py": "Write a program to count vowels in a string.",
        "challenge_8.py": "Write a function to calculate the GCD of two numbers.",
        "challenge_9.py": "Write a program to transpose a matrix.",
        "challenge_10.py": "Write a function to flatten a nested list.",
        "challenge_11.py": "Write a program to convert a decimal to binary.",
        "challenge_12.py": "Write a function to calculate the sum of digits of a number.",
        "challenge_13.py": "Write a program to implement binary search.",
        "challenge_14.py": "Write a function to find duplicates in a list.",
        "challenge_15.py": "Write a program to solve the Tower of Hanoi problem.",
        "challenge_16.py": "Write a function to merge two sorted lists.",
        "challenge_17.py": "Write a program to calculate the area of a triangle given its sides.",
        "challenge_18.py": "Write a function to validate an email address.",
        "challenge_19.py": "Write a program to implement a stack using a list.",
        "challenge_20.py": "Write a program to calculate the square root of a number without using built-in functions."
    }

    # Select a random challenge
    random_challenge_file = random.choice(challenge_files)
    print(f"\nChallenge: {challenge_prompts[random_challenge_file]}")
    print("Write your code below. Type 'END' (case-insensitive) on a new line to finish:\n")

    # Collect user input for their solution
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    # Save the solution to the corresponding file
    code = "\n".join(lines)
    with open(random_challenge_file, "w") as f:
        f.write(code)

    print(f"\nCode saved to {random_challenge_file}.")

    # Update progress tracker
    progress["challenges_completed"] += 1
    print(f"Challenges completed so far: {progress['challenges_completed']}")

# Help menu
def help_menu():
    print("\n\033[1mHelp Menu:\033[0m")
    print("1. Select topics from the main menu to learn specific concepts.")
    print("2. Take quizzes to test your knowledge.")
    print("3. Complete challenges to practice coding.")
    print("4. Use 'View Progress' to check your learning journey.")
    print("5. Exit to close the tool.")

# Open saved code
def open_saved_code():
    print("\n\033[1mOpen Saved Code:\033[0m")
    print("Files in the current directory:")
    files = [f for f in os.listdir(".") if f.endswith(".py")]
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print("0. Exit")
    try:
        choice = int(input("Select a file to open: "))
        if 0 < choice <= len(files):
            file_name = files[choice - 1]
            with open(file_name, "r") as f:
                print(f"\nContents of {file_name}:\n")
                print(f.read())
        elif choice == 0:
            print("Exiting file viewer.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")

# Progress view
def view_progress():
    print("\n\033[1mYour Progress:\033[0m")
    print("Topics Learned:", ", ".join(progress["topics_learned"]) or "None")
    print("Quiz Score:", progress["quiz_score"])
    print("Challenges Completed:", progress["challenges_completed"])

# Main program loop
while True:
    choice = main_menu()
    if choice == 1:
        print("\033[2J\033[H", end="")
        learn_strings()
    elif choice == 2:
        print("\033[2J\033[H", end="")
        learn_loops()
    elif choice == 3:
        print("\033[2J\033[H", end="")
        learn_recursion()
    elif choice == 4:
        print("\033[2J\033[H", end="")
        learn_data_types()
    elif choice == 5:
        print("\033[2J\033[H", end="")
        learn_file_handling()
    elif choice == 6:
        print("\033[2J\033[H", end="")
        learn_error_handling()
    elif choice == 7:
        print("\033[2J\033[H", end="")
        quiz()
    elif choice == 8:
        print("\033[2J\033[H", end="")
        challenges()
    elif choice == 9:
        print("\033[2J\033[H", end="")
        print("\nFiles in the current directory:")
        print("\n".join(os.listdir(".")))
    elif choice == 10:
        print("\033[2J\033[H", end="")
        help_menu()
    elif choice == 11:
        print("\033[2J\033[H", end="")
        view_progress()
    elif choice == 12:
        print("\033[2J\033[H", end="")
        open_saved_code()
    elif choice == 13:
        print("\033[2J\033[H", end="")
        print("""\

 _____ _                 _                           __            
|_   _| |__   __ _ _ __ | | __  _   _  ___  _   _   / _| ___  _ __ 
  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | |_ / _ \| '__|
  | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |  _| (_) | |   
  |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/_\__,_| |_|  \___/|_|   
 _   _ ___(_)_ __   __ _   _ __ |___/_| |_| |__   ___  _ __        
| | | / __| | '_ \ / _` | | '_ \| | | | __| '_ \ / _ \| '_ \       
| |_| \__ \ | | | | (_| | | |_) | |_| | |_| | | | (_) | | | |      
 \__,_|___/_|_| |_|\__, | | .__/ \__, |\__|_| |_|\___/|_| |_|      
 _       _         |___/  |_|   _|___/                             
(_)_ __ | |_ ___ _ __ __ _  ___| |_(_)_   _____                    
| | '_ \| __/ _ \ '__/ _` |/ __| __| \ \ / / _ \                   
| | | | | ||  __/ | | (_| | (__| |_| |\ V /  __/                   
|_|_| |_|\__\___|_|  \__,_|\___|\__|_| \_/ \___|        _          
| | ___  __ _ _ __ _ __ (_)_ __   __ _  | |_ ___   ___ | |         
| |/ _ \/ _` | '__| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |         
| |  __/ (_| | |  | | | | | | | | (_| | | || (_) | (_) | |         
|_|\___|\__,_|_|  |_| |_|_|_| |_|\__, |  \__\___/ \___/|_|         
                                 |___/                             


  
""")
