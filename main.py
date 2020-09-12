# Rock Paper Scissors Game in python and tkinter

import tkinter as tk
import random
import sys 
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import scrolledtext

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("800x400")
window.resizable(0,0)
window.configure(bg="dodgerblue")

lbl = tk.Label(window, text="BOT", font=("Arial Bold", 25))
lbl.place(x=10, y=200)

def Buttons():
    global rock 
    global paper 
    global scissors
    rock_state = IntVar()
    rock = tk.Button(window, text="Rock", font=("Arial Bold", 30), command=rock_click)
    rock.place(x=120, y=40)
    paper = tk.Button(window, text="Paper", font=("Arial Bold", 30), command=paper_click)
    paper.place(x=280, y=40)
    scissors = tk.Button(window, text="Scissors", font=("Arial Bold", 30), command=scissors_click)
    scissors.place(x=450, y=40)

def entry():
    global bot
    global guesses
    guesses = ["Rock", "Paper", "Scissors"]
    bot = Entry(window, width=20, font=("Arial Bold", 30))
    bot.place(x=120, y=200)

# score
global score 
score = 0
lbl = tk.Label(window, text="Score : {}".format(score), font=("Arial Bold", 15))
lbl.place(x=10, y=300)

def rock_click():
    global score 
    bot_guess = random.choice(guesses)
    bot.insert(INSERT, bot_guess)
    if bot.get() == "Rock":
        messagebox.showinfo("EQUAL", "EQUAL")
        bot.delete(0, END)

    elif bot.get() == "Paper":
        messagebox.showinfo("LOST", "YOU LOST")
        bot.delete(0, END)

    elif bot.get() == "Scissors":
        messagebox.showinfo("WON", "YOU WON")
        score += 1
        lbl.configure(text="Score : {}".format(score), font=("Arial Bold", 15))
        bot.delete(0, END)

def paper_click():
    global score 
    bot_guess = random.choice(guesses)
    bot.insert(INSERT, bot_guess)

    if bot.get() == "Paper":
        messagebox.showinfo("EQUAL", "EQUAL")
        bot.delete(0, END)

    elif bot.get() == "Rock":
        messagebox.showinfo("WON", "YOU WON")
        score += 1
        lbl.configure(text="Score : {}".format(score), font=("Arial Bold", 15))
        bot.delete(0, END)

    elif bot.get() == "Scissors":
        messagebox.showinfo("LOST", "YOU LOST")
        bot.delete(0, END)

def scissors_click():
    global score 
    bot_guess = random.choice(guesses)
    bot.insert(INSERT, bot_guess)

    if bot.get() == "Scissors":
        messagebox.showinfo("EQUAL", "EQUAL")
        bot.delete(0, END)

    elif bot.get() == "Rock":
        messagebox.showinfo("LOST", "YOU LOST")
        bot.delete(0, END)

    elif bot.get() == "Paper":
        messagebox.showinfo("WON", "YOU WON")
        score += 1
        lbl.configure(text="Score : {}".format(score), font=("Arial Bold", 15))
        bot.delete(0, END)


Buttons()
entry()

window.mainloop()
