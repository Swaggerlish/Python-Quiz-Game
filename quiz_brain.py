class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list) - 1:
            self.question_number += 1
            return True
        else:
            print("You have reached the end of the question")
            print(f"Your total score is {self.score}/{self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer_to_question = input(f"Q. {self.question_number + 1}: The next question is '{current_question.question}'"
                                   f" what is your answer? True or False:\n")

        self.check_answer(answer_to_question, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"you got it right! your score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong! Your score is {self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}")




