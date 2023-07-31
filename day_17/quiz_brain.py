class Quizbrain:
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        return self.question_num < len(self.question_list)
    
        
        
        
        
    def next_quest(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Qno.{self.question_num}:{current_question.text}. Type your ans (true/false):")
        self.check_ans(user_ans,current_question.answer)
    
    
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("u got it right")
            self.score +=1
            print("\n")
        else:
            print("that is wrong")
            print("\n")
        print(f"the correct ans is {correct_ans}")
        print(f" your current score is {self.score}/{self.question_num}")
        print("\n")
            
        

        