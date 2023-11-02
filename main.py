import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")

        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 18))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.generate_question()
    
    def generate_question(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operator = random.choice(['+', '-', '*', '/'])
        self.question = f"{self.num1} {self.operator} {self.num2}"
        self.question_label.config(text=self.question)
    
    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = eval(user_answer)
            correct_answer = eval(self.question)
            if user_answer == correct_answer:
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text="Incorrect! The correct answer is: " + str(correct_answer), fg="red")
        except:
            self.result_label.config(text="Invalid input", fg="red")
        self.answer_entry.delete(0, tk.END)
        self.generate_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
