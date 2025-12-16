def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. Java", "C. JavaScript", "D. All"],
            "answer": "D"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. def", "B. func", "C. define", "D. function"],
            "answer": "A"
        }
    ]

    score = 0
    print("🎯 Welcome to the Quiz Game")
    print("--------------------------")
    print("Rules:")
    print("• Each correct answer gives 1 point")
    print("• No negative marking\n")

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print("🎉 Quiz Completed!")
    print(f"Your Final Score: {score}/{len(questions)}")

    if score == len(questions):
        print("Excellent performance!")
    elif score >= 1:
        print("Good effort! Keep learning.")
    else:
        print("Better luck next time.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        quiz_game()
    else:
        print("Thanks for playing!")

quiz_game()
