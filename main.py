from question_model import Question
from data  import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text,question_ans)
    question_bank.append(new_question)
    

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_quest()
    
print("you completed the quiz")
print(f"your final score is {quiz.score}/{len(question_bank)}")
    
