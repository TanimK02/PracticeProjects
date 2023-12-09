from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, height=250, width=300)
        self.score = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)
        self.display = Canvas(bg='white', highlightthickness=0, height=250, width=300)
        self.question = self.display.create_text(150, 125, font=('Arial', 20, 'italic'), fill='black',
                                                 width=280)
        self.display.grid(column=0, row=1, columnspan=2, pady=50)
        false_img = PhotoImage(file='images/false.png')
        self.false = Button(image=false_img, command=self.check_wrong)
        self.false.grid(column=0, row=2)
        true_img = PhotoImage(file='images/true.png')
        self.true = Button(image=true_img, command=self.check_right)
        self.true.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()


    def next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.display.config(bg='white')
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.display.itemconfig(self.question, text=q)

        else:
            self.display.itemconfig(self.question,text="You've finished the test.")
            self.true.config(state='disabled')
            self.false.config(state='disabled')


    def check_wrong(self):
        self.feedback(self.quiz.check_answer('false'))

    def check_right(self):
        self.feedback(self.quiz.check_answer('true'))

    def feedback(self,answer):
        if answer is True:
            self.display.config(bg='green')
        else:
            self.display.config(bg='red')
        self.window.after(1000, self.next_question)
