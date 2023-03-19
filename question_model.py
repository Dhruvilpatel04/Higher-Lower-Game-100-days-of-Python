class Question:
    def __init__(self,q_text,q_ans):
        self.text = q_text
        self.answer = q_ans
        
new_q = Question("2+4","6")
print(new_q.text)
 