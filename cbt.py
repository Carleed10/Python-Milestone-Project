questions = [
    {
        "question": "1. What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n",
        "answer": "b"
    },
    {
        "question": "2.What color is the sky on a clear day?\n(a) Red\n(b) Blue\n(c) Green\n(d) Yellow\n",
        "answer": "b"
    },
    {
        "question": "3. How many legs does a spider have?\n(a) 6\n(b) 7\n(c) 8\n(d) 9\n",
        "answer": "c"
    },
    {
        "question": "4. What sound does a cow make?\n(a) Meow\n(b) Bark\n(c) Moo\n(d) Quack\n",
        "answer": "c"
    },
    {
        "question": "5. What is the opposite of 'hot'?.\n(a) Warm\n(b) Cold\n(c) Cool\n(d) Boiling\n",
        "answer": "b"
    },
    {
        "question": "4. Who wrote 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) J.K. Rowling\n(c) Mark Twain\n(d) Charles Dickens\n",
        "answer": "a"
    }
]

score = 0


for question in questions:
    while True:  # Loop until a valid answer is provided
        user_answer = input(f"{question['question']} Enter your answer : ").lower()

        if user_answer in ["a", "b", "c", "d"]:
            break  # Valid answer, break out of the loop
        else:
            print("Invalid input. Please enter a valid option (a, b, c, or d).")

    if user_answer == question["answer"]:
        score += 1
    else:
        print(f"Wrong! The correct answer was '{question['answer']}'\n")

# Display the user's score at the end
print(f"Quiz completed! Your total score is {score} out of {len(questions)}.")

