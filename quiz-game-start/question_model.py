# We create the model for Question with 2 parameters: the text of the question and the answer.
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
