# here we will create a class which will manage all the questioning and quizzing functionality

class QuizBrain:
    def __init__(self, q_list):
        # the quizz starts from the first question (question_number = 0) and it needs to keep track of which questions
        # the user is currently on,and we will use that number to go through the list of questions which will be passed
        # over to QuizBrain object when it gets initialized
        self.question_number = 0  # this will be a default value (first question, 0)
        self.question_list = q_list  # this will be passed in the form of an input
        self.score = 0  # score attribute to track user's score, starting at 0
    # now we want to create another method which will jump to the next question once the user types the answer to
    # previous question. And in main.py we will create a while loop that checks if the quizz still has questions remaining
    # it will return a boolean depending on the value of question_number
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
    # we can simplify the code above and write it as: "return self.question_number < len(self.question_list)"


    # now we define a method called next_question which will retrieve the question from question_list depending on the
    # number of question we are currently in, and we show the question text to the user in the form of an input, asking
    # as well for the answer (True/False)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # we need this to show the correct number to of the question to the user
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)  # we call the method check answer by passing 2 values,
        # the user's answer and the correct answer, which is current.question.answer (because current_question is an
        # object which has a text and an answer attribute). Now that we pass it here we can receive it inside our method
        # check_answer as parameters (user_answer, correct_answer)

    # we also need a method to check if the answer is correct. For that we need to keep track on the user score, so we
    # add another attribute "score" which will start at value 0 and will increase when user gets a question right.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}. ")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")  # print a space between questions