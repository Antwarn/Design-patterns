# Designmønstre i Udviklingen af en Lærings App

Dette projekt fokuserer på anvendelsen af designmønstre til at designe og implementere en læringsapp inden for et selvvalgt emne, niveau og alderstrin. Projektet har til formål at demonstrere, hvordan designmønstre kan bruges i praksis for at skabe en effektiv løsning. I dette eksempel bruger jeg Python med tkinter til brugergrænsefladen.

## Projektformål og Målgruppe

Projektets formål er at udvikle en interaktiv læringsapp målrettet folkeskoleelever for at lære matematiske grundlæggende som addition og subtraktion, multiplikation og division. 

## Valg af Designmønstre

I dette projekt vil jeg anvende følgende designmønstre:

1. **Kommando-mønsteret:** Dette mønster adskiller en anmodning om at udføre en handling fra selve handlingen. Jeg bruger det til at håndtere brugerinteraktioner, f.eks. når brugeren skal svare på matematiske spørgsmål. Hver handling, såsom at besvare et spørgsmål, implementeres som en kommandoklasse med en `execute`-metode.

2. **Fabriksmønsteret:** Dette mønster bruges til at oprette forskellige typer af spilobjekter, i vores tilfælde forskellige typer matematiske spørgsmål.

## Implementering

Jeg har oprettet en interaktiv læringsapp, der indeholder matematiske spørgsmål om addition og subtraktion, multiplikation og division. Hver matematisk operation er repræsenteret som en kommandoklasse, der udfører handlingen. Brugeren kan interagere med appen ved at besvare spørgsmål ved hjælp af en GUI-grænseflade oprettet med tkinter i Python.

## Test og Tilpasning

Når appen er udviklet, skal den testes for at sikre, at den fungerer som forventet. Du kan tilpasse appen ved at ændre spørgsmålene eller tilføje nye designmønstre, hvis det er relevant.

## Refleksion

Brugen af designmønstre i dette projekt har gjort det muligt at opdele kompleks funktionalitet i mindre, håndterbare komponenter. Kommandomønsteret har gjort det lettere at håndtere brugerinteraktioner og sikre, at de udføres korrekt.

## Forfatter

Dette projekt er udviklet af `Anton Merkelsen 3.M Sukkertoppen`.

