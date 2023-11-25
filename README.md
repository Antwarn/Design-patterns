# Designmønstre i Udviklingen af en Lærings App

Jeg skulle i denne opgave programmere en lærings app med fokus på design patterns. Læarings appen skulle være et selv valgt emne og niveau. Hovede fokus i opgaven er hvordan design patterns kan bruges til at implementere løsningen i praksis. 

## Projektformål og Målgruppe

Projektets formål er at ved brug af design patterns udvikle en interaktiv læringsapp målrettet folkeskoleelever for at lære matematiske grundlæggende som addition og subtraktion og multiplikation. 

## Valg af Designmønstre

I dette projekt vil jeg anvende følgende designmønstre:

1. **Kommando-mønsteret:** Dette mønster adskiller en anmodning om at udføre en handling fra selve handlingen. Jeg bruger det til at håndtere brugerinteraktioner, f.eks. når brugeren skal svare på matematiske spørgsmål. Hver handling, såsom at besvare et spørgsmål, implementeres som en kommandoklasse med en `execute`-metode.

2. **Fabriksmønsteret:** Dette mønster bruges til at oprette forskellige typer af spilobjekter, i vores tilfælde forskellige typer matematiske spørgsmål.

## Eksempel på kode

1. **Implimentering af komando-mønsteret:** I denne del af koden bruges Kommando-mønsteret til at adskille evalueringen af brugerens svar og opdatering af GUI'en fra resten af programmet, dette gør det nemmer at udvide koden i fremtiden.
```python
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
```

2. **Implimentering af fabriksmønsteret:** I denne del af koden bruger jeg fabriksmønsteret til at oprette tkinter-widget-objekter i en sperat klasse kaldet `WidgetFactory`. Det gør at oprettelsen af widgets bliver adskillet fra brugerkoden som gør det nemmer at ændre koden og genbruge oprettelsesprocessen af de forskellige typer widgets.
```python
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
```
## Implementering

Jeg har oprettet en interaktiv læringsapp, der indeholder matematiske spørgsmål om addition og subtraktion og multiplikation. Hver matematisk operation er repræsenteret som en kommandoklasse, der udfører handlingen. Brugeren kan interagere med appen ved at besvare spørgsmål ved hjælp af en GUI-grænseflade oprettet med tkinter i Python.

## Test og Tilpasning

Når appen er udviklet, skal den testes for at sikre, at den fungerer som forventet. 
Jeg har levet to test af programmet. Første test genererede den spørgsmålet `3 + 2` der gav jeg inputtet 5 som var det rigtige svar. I den anden test svarede jeg intentionelt forkert på spørgsmålet `10 * 5` den sagde som forventet at svaret var forkert. jeg har lavet et test skema som er vedlagt under dette afsnit.  

| Input | Forventet Output | Reelt output |
| ----- | ---------------- | ------------ |
|   5   | "Correct input" grøn tekst   | "Correct input" grøn tekst | 
|   10  | "Invalid input" rød tekst    | "Invalid input" rød tekst  |

## Refleksion

Brugen af designmønstre i dette projekt har gjort det muligt at opdele kompleks funktionalitet i mindre, håndterbare komponenter. Kommandomønsteret har gjort det lettere at håndtere brugerinteraktioner og sikre, at de udføres korrekt.

## Forfatter

Dette projekt er udviklet af `Anton Merkelsen 3.M Sukkertoppen`.

