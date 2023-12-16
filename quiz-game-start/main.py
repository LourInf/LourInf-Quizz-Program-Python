# import data list with dictionaries
from data import question_data
# import the Question model
from question_model import Question
# import the QuizBrain model
from quiz_brain import QuizBrain

# here we don't want to see a list of dictionaries (what we have in data.py), but a list of question objects.
# We create a new object by constructing one from the Question and then giving it the required inputs
# the question bank should contain a list of question objects, each being initialized with a question and answer

question_bank = []  # we create an empty list which later will become a list of question objects.
for question in question_data:  # we create a for loop to iterate over each question inside the question_data dictionaries
    question_text = question["text"]  # we create a variable for each of the questions. We want to get their key "text", which contains the question
    question_answer = question["answer"]  # we create another variable. Here we want to get their key "answer", which contains the answer
    new_question = Question(question_text, question_answer)  # we create our object and save it in a variable called new_question, which is created from the Question class, expecting 2 parameters (q_text = question_text, q_answer = question_answer)
    question_bank.append(new_question)  # now that our object is created we can add it to our question_bank, so we append each question that we create with our for loop

# here we initialize our QuizBrain and the value that we will put in there as the q_list is going to be the question_bank
# this way it will receive the question_bank, and it will be inside the q_list attribute
quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # if quiz still has questions left, keep showing the next questions
    quiz.next_question()

#at the end of the quiz qe want to show the user the final score
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")