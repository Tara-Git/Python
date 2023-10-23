from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # this is a list of questions
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_data)
print(type(question_data))
print(type(question_data[0]))
print(question_data[0]["question"])
print(type(question_data[0]["question"]))
print(question_bank)
print(type(question_bank))
print(type(question_bank[0]))
print(question_bank[0].text)
print(type(question_bank[0].text))



""" I find that we also can go a head with out converting the question list to an obj, The following is using Obj
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
"""


quiz_02 = QuizBrain(question_data)

while quiz_02.still_has_questions():
    quiz_02.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_02.score}/{quiz_02.question_number}")
