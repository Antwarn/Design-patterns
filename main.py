import tkinter as tk
import random

# Fabriksmønster: WidgetFactory
class WidgetFactory:
    @staticmethod
    def create_label(root, text, font):
        return tk.Label(root, text=text, font=font)

    @staticmethod
    def create_entry(root, font):
        return tk.Entry(root, font=font)

    @staticmethod
    def create_button(root, text, command):
        return tk.Button(root, text=text, command=command)

# Kommandomønster: CheckAnswerCommand
class CheckAnswerCommand:
    def __init__(self, app):
        self.app = app

    def execute(self):
        user_answer = self.app.answer_entry.get()
        try:
            user_answer = eval(user_answer)
            correct_answer = eval(self.app.question)
            if user_answer == correct_answer:
                self.app.result_label.config(text="Correct!", fg="green")
            else:
                self.app.result_label.config(text="Incorrect! The correct answer is: " + str(correct_answer), fg="red")
        except:
            self.app.result_label.config(text="Invalid input", fg="red")
        self.app.answer_entry.delete(0, tk.END)
        self.app.generate_question()

# Opret en class kaldet MathQuizApp
class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")

        # Fabriksmønster: Opret instanser af widgets ved hjælp af fabrik-objektet
        self.question_label = WidgetFactory.create_label(root, "", ("Arial", 24))
        self.question_label.pack(pady=20)

        self.answer_entry = WidgetFactory.create_entry(root, ("Arial", 18))
        self.answer_entry.pack(pady=10)

        # Kommandomønster: Opret en kommando med reference til denne app
        check_command = CheckAnswerCommand(self)

        self.check_button = WidgetFactory.create_button(root, "Check Answer", check_command.execute)
        self.check_button.pack()

        self.result_label = WidgetFactory.create_label(root, "", ("Arial", 16))
        self.result_label.pack(pady=20)

        self.generate_question()

    def generate_question(self):
        # Generer to tilfældige tal mellem 1 og 10
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        # Vælg en tilfældig matematisk operator (+, -, *)
        self.operator = random.choice(['+', '-', '*'])
        # Sammensæt spørgsmålet som en tekststreng
        self.question = f"{self.num1} {self.operator} {self.num2}"
        # Opdater labelen med det nye spørgsmål
        self.question_label.config(text=self.question)

# Kør koden kun, hvis den udføres som et selvstændigt program (ikke som en import)
if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
