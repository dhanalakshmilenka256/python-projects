'''class User:#captilize-pascalcase,lower-camelcase,everything-snake_case
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("159","Dhana")
user_2=User("200","Lakshmi")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)'''
from quiz_game import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_qusetions():
    quiz.next_question()

print("you've completed quiz")
print(f"your final score was:{quiz.score}/{quiz.question_number}")



