from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# question_bank = []
# for i in range(len(question_data)):
#     question_bank.append( Question(question_data[i]["text"], question_data[i]["answer"]))     //This also works

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Congratulations!!!. You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")