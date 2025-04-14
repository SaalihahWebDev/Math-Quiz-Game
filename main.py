import random
print("🧠 Welcome to the Easy Math Quiz for Kids!")
score = 0
for i in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])
        if operation == "+":
              correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2
answer=int(input(f"Question {i+1}:What is {num1} {operation} {num2}"))
if answer == correct_answer:
                print("✅Correct!")
                score += 1
else:
        print(f"❌ Oops! The correct answer was {correct_answer}. ")
print(f"Quiz over.Your Score is{score}/5")