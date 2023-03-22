

class Question:
    def __init__(self, ques_text: str, answer: str):
        self.ques_text = ques_text
        self.answer = answer

    def __repr__(self):
        return '{'+ self.ques_text +', '+ self.answer +'}'
    
quizQuestions = [
                Question("Question 1. What city is the capital of Australia", "Canberra"),
                Question("Question 2. What city is the capital of Japan", "Tokyo"),
                Question("Question 3. How many islands does the Philippines have", "7100")
                ]

for question in quizQuestions:
    print(f"{question.ques_text}?")
    userInput = input()

    if (userInput.lower() == question.answer.lower()):
        print("That is correct!")
    else:
        print(f"Sorry, the correct answer is {question.answer}.")