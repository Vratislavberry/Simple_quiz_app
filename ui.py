from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
LIGHT_GRAY = "#cfcfcf"
FONT = ("New Times Roman", 15, "normal")
FONT_QUESTION = ("New Times Roman", 25, "normal")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
            self.quiz = quiz_brain
            self.window =Tk()
            self.window.title("Quizzler")
            self.window.config(bg=THEME_COLOR)
            self.window.minsize(width=350, height=500)

            # Creating widgets
            self.lbl_score = Label(text="Your current score: is 0/0", bg=THEME_COLOR, fg=LIGHT_GRAY, font=FONT)
            self.canvas = Canvas(width=300, height=250, bg="white")

            self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=FONT, width=280)

            self.img_false = PhotoImage(file="images/false.png")
            self.btn_false = Button(image=self.img_false, highlightthickness=0, bd=0,
                                    command=lambda: self.check_answer("False")) # bd = border

            self.img_true = PhotoImage(file="images/true.png")
            self.btn_true = Button(image=self.img_true, highlightthickness=0,
                                   bd=0, command=lambda: self.check_answer("True"))


            # Putting widgets on screen
            self.lbl_score.grid(row=0, column=1)
            self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)
            self.btn_false.grid(row=2, column=0)
            self.btn_true.grid(row=2, column=1)


            self.get_next_question()

            self.window.mainloop()

    def check_answer(self, answer: str):
            score, right_answer = self.quiz.check_answer(answer)
            self.lbl_score.config(text=score)
            self.change_color(right_answer)

            self.window.after(1000, self.set_default_color)

            self.get_next_question()
            if not self.quiz.still_has_questions():
                self.btn_true.config(state=DISABLED)
                self.btn_false.config(state=DISABLED)
                self.canvas.itemconfig(self.question_text, text="Konec kvízu")
            else:
                self.btn_true.config(state=NORMAL)
                self.btn_false.config(state=NORMAL)





    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def change_color(self, answer):
        self.btn_true.config(state=DISABLED)
        self.btn_false.config(state=DISABLED)
        if answer:
            self.canvas.config(bg="#3afc05")
        else:
            self.canvas.config(bg="#fc052e")


    def set_default_color(self):
        self.canvas.config(bg="white")



