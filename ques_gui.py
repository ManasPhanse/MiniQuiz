import tkinter as tk
from tkinter import messagebox
import random

# Questions, options, and answers
ques_list = [
    "What is the capital of India?",
    "What is the Economic capital of India?",
    "Which Indian states have snow?"
]

ans_list = ["New Delhi", "Mumbai", {"Kashmir", "Himachal Pradesh", "Uttarakhand"}]

opt_list = [
    ["New Delhi", "Mumbai", "Kolkata", "London"],
    ["Mumbai", "New Delhi", "Ujjain", "Varanasi"],
    ["Kashmir", "Himachal Pradesh", "Uttarakhand", "Kerala"]
]

# Shuffle questions and corresponding options and answers
combined = list(zip(ques_list, opt_list, ans_list))
random.shuffle(combined)
ques_list, opt_list, ans_list = zip(*combined)

# GUI App
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_frame = tk.Frame(root, bg="#383838")
        self.main_frame.grid(sticky='nsew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.question_index = 0
        self.score = 0
        self.marks = []

        self.question_label = tk.Label(self.main_frame, text=ques_list[self.question_index], wraplength=400, font=("Helvetica", 14), fg="white", bg="#383838")
        self.question_label.grid(row=0, column=0, pady=20)

        self.var = tk.StringVar()
        self.vars = [tk.StringVar(value="") for _ in opt_list[self.question_index]]

        self.options_frame = tk.Frame(self.main_frame, bg="#383838")
        self.options_frame.grid(row=1, column=0, sticky="nsew")

        self.option_widgets = []

        self.create_option_widgets()

        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.check_answer, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.submit_button.grid(row=2, column=0, pady=20)

    def create_option_widgets(self):
        for widget in self.option_widgets:
            widget.destroy()

        self.option_widgets = []

        if isinstance(ans_list[self.question_index], set):
            for i, opt in enumerate(opt_list[self.question_index]):
                checkbox = tk.Checkbutton(self.options_frame, text=opt, variable=self.vars[i], onvalue=opt, offvalue="", bg="#f0f0f0", font=("Helvetica", 12))
                checkbox.pack(anchor="w", pady=2)
                self.option_widgets.append(checkbox)
        else:
            for i, opt in enumerate(opt_list[self.question_index]):
                radiobutton = tk.Radiobutton(self.options_frame, text=opt, variable=self.var, value=opt, bg="#f0f0f0", font=("Helvetica", 12))
                radiobutton.pack(anchor="w", pady=2)
                self.option_widgets.append(radiobutton)

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(ques_list):
            self.question_label.config(text=ques_list[self.question_index])
            self.var.set("")
            for var in self.vars:
                var.set("")
            self.create_option_widgets()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {sum(self.marks)}")
            self.root.destroy()

    def check_answer(self):
    	if isinstance(ans_list[self.question_index], set):
        	selected = set(var.get() for var in self.vars if var.get())
        	correct_ans = ans_list[self.question_index]

        	if selected == correct_ans:
            		self.marks.append(5)
        	else:
            		self.marks.append(-1)
    	else:
        	selected = self.var.get()
        	correct_ans = ans_list[self.question_index]

        	if selected == correct_ans:
            		self.marks.append(5)
        	else:
            		self.marks.append(-1)

    	self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#383838")
    app = QuizApp(root)
    root.mainloop()
