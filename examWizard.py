questions = [
    {
        "question": "1. Explain the concept of Object-Oriented Programming (OOP).",
        "keywords": {"class": 2, "object": 2, "inheritance": 1, "polymorphism": 1, "encapsulation": 1}
    },
    {
        "question": "2. What is a database, and why is it important?",
        "keywords": {"storage": 2, "data": 2, "retrieval": 1, "query": 1, "management": 1}
    },
    {
        "question": "3. Explain the working of a computer network.",
        "keywords": {"communication": 2, "protocol": 2, "IP": 1, "router": 1, "topology": 1}
    },
    {
        "question": "4. Describe how a web browser works.",
        "keywords": {"HTTP": 2, "rendering": 2, "URL": 1, "client-server": 1, "request": 1}
    },
    {
        "question": "5. What is machine learning, and how does it differ from traditional programming?",
        "keywords": {"data": 2, "algorithm": 2, "training": 1, "model": 1, "pattern recognition": 1}
    }
]

def evaluate_answer(answer, keywords):
    score = 0
    for keyword, weight in keywords.items():
        if keyword.lower() in answer.lower():
            score += weight
    return score


total_score = 0
max_score = sum([sum(q['keywords'].values()) for q in questions])


print("Welcome to the Exam Wizard. Please answer the following questions:\n")

for question in questions:
    print(question["question"])
    user_answer = input("Your answer: ")


    score = evaluate_answer(user_answer, question["keywords"])
    total_score += score

    print(f"Score for this question: {score} out of {sum(question['keywords'].values())}\n")

print(f"Exam completed! Your total score is {total_score} out of {max_score}.")
