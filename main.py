# Importer tkinter-biblioteket som tk
import tkinter as tk
# Importer random-biblioteket for at generere tilfældige tal
import random

# Opret en klasse kaldet MathQuizApp
class MathQuizApp:
    # Konstruktørmetode for initialisering af appen
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")  # Indstil titlen på vinduet til "Math Quiz"

        # Opret en label til at vise spørgsmålet, indstil skrifttype og pak den i vinduet
        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        # Opret en indtastningsboks til brugerens svar, indstil skrifttype og pak den i vinduet
        self.answer_entry = tk.Entry(root, font=("Arial", 18))
        self.answer_entry.pack(pady=10)

        # Opret en knap med teksten "Check Answer" og angiv, at den skal udføre check_answer-metoden ved klik
        self.check_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        # Opret en label til at vise resultatet af brugerens svar, indstil skrifttype og pak den i vinduet
        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        # Generer det første spørgsmål
        self.generate_question()

    # Metode til at generere et nyt matematisk spørgsmål
    def generate_question(self):
        # Generer to tilfældige tal mellem 1 og 10
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        # Vælg en tilfældig matematisk operator (+, -, *, /)
        self.operator = random.choice(['+', '-', '*', '/'])
        # Sammensæt spørgsmålet som en tekststreng
        self.question = f"{self.num1} {self.operator} {self.num2}"
        # Opdater labelen med det nye spørgsmål
        self.question_label.config(text=self.question)

    # Metode til at kontrollere brugerens svar
    def check_answer(self):
        user_answer = self.answer_entry.get()  # Hent brugerens svar fra indtastningsboksen
        try:
            user_answer = eval(user_answer)  # Evaluer brugerens svar som en matematisk udtryk
            correct_answer = eval(self.question)  # Evaluer det korrekte svar som en matematisk udtryk
            if user_answer == correct_answer:
                self.result_label.config(text="Correct!", fg="green")  # Hvis svaret er korrekt, vis "Correct!" i grønt
            else:
                self.result_label.config(text="Incorrect! The correct answer is: " + str(correct_answer), fg="red")  # Hvis svaret er forkert, vis "Incorrect!" i rødt og det korrekte svar
        except:
            self.result_label.config(text="Invalid input", fg="red")  # Hvis der opstår en fejl, vis "Invalid input" i rødt
        self.answer_entry.delete(0, tk.END)  # Ryd indtastningsboksen
        self.generate_question()  # Generer et nyt spørgsmål

# Kør koden kun, hvis den udføres som et selvstændigt program (ikke som en import)
if __name__ == "__main__":
    root = tk.Tk()  # Opret en tkinter-rodwidget (vindue)
    app = MathQuizApp(root)  # Opret en instans af MathQuizApp-klassen
    root.mainloop()  # Start hovedloopet for tkinter-vinduet
