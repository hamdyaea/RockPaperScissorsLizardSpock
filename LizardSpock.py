#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import tkinter as tk
import tkinter
from tkinter import messagebox
import random


class Game:
    def __ini__(self):
        self.ciseaux_tk
        self.caillou_tk
        self.feuille_tk
        self.lizard_tk
        self.spock_tk
        self.user_score
        self.sheldon_score
        self.comp


top = tk.Tk()
top.title("Rock - Paper - Scissors - Lizard - Spock")

Game.ciseaux_tk = tk.PhotoImage(file="./images/scissors.gif")
Game.caillou_tk = tk.PhotoImage(file="./images/rock.gif")
Game.feuille_tk = tk.PhotoImage(file="./images/paper.gif")
Game.lizard_tk = tk.PhotoImage(file="./images/lizard.gif")
Game.spock_tk = tk.PhotoImage(file="./images/spock.gif")

Game.sheldon_score = 0
Game.user_score = 0


def Rock():
    Game.comp = random.randint(1, 5)
    if Game.comp == 3:
        Game.comp = "Scissors"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nRock crushes Scissors \n"
            + "Your Choice:Rock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 1:
        Game.comp = "Rock"
        messagebox.showinfo(
            "Same choice!",
            "EGUALITY!\n"
            + "Your Choice:Rock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 2:
        Game.comp = "Lizard"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nRock crushes Lizard \n"
            + "Your Choice:Rock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE! \nSpock vaporizes Rock \n"
            + "Your Choice:Rock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    else:
        Game.comp = "Paper"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nPaper covers Rock \n"
            + "Your Choice:Rock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )


def paper():
    Game.comp = random.randint(1, 5)
    if Game.comp == 1:
        Game.comp = "Rock"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nPaper covers Rock \n"
            + "Your Choice: Paper\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 2:
        Game.comp = "Paper"
        messagebox.showinfo(
            "Same choice!",
            "EGUALITY!\n"
            + "Your Choice: Paper\n"
            + "\nSheldon's Choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 3:
        Game.comp = "Lizard"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nLizard eats Paper\n"
            + "Your Choice: Paper\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nPaper disproves Spock \n"
            + "Your Choice: Paper\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    else:
        Game.comp = "Scissors"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nScissors cuts Paper \n"
            + "Your Choice: Paper\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )


def scissors():
    Game.comp = random.randint(1, 5)
    if Game.comp == 2:
        Game.comp = "Paper"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nScissors cuts Paper \nYour Choice: Scissors\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        messagebox.showinfo(
            "Same choice!",
            "EGUALITY!\nYour Choice: Scissors\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nScissors decapitates Lizard \n"
            + "Your Choice:Scissors\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nSpock smashes Scissors \n"
            + "Your Choice:Scissors\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    else:
        Game.comp = "Rock"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nRock crushes Scissors \nYour Choice: Scissors\n"
            + "\nSheldon's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )


def lizard():
    Game.comp = random.randint(1, 5)
    if Game.comp == 2:
        Game.comp = "Paper"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nLizard eats Paper \nYour Choice: Lizard\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nScissors decapitates Lizard \nYour Choice: Lizard\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        messagebox.showinfo(
            "Same choice!",
            "EGUALITY!\n"
            + "Your Choice: Lizard\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nLizard poisons Spock \n"
            + "Your Choice:Lizard\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    else:
        Game.comp = "Rock"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nRock crushes Lizard \nYour Choice: Lizard\n"
            + "\nSheldon's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )


def spock():
    Game.comp = random.randint(1, 5)

    if Game.comp == 2:
        Game.comp = "Paper"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nPaper disproves Spock \nYour Choice: Spock\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 3:
        Game.comp = "Scissors"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN !\nSpock smashes Scissors \nYour Choice: Spock\n"
            + "\nSheldon's choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 1:
        Game.comp = "Lizard"
        Game.sheldon_score += 1
        messagebox.showinfo(
            "Unlucky!",
            "YOU LOSE!\nLizard poisons Spock \n"
            + "Your Choice: Spock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    elif Game.comp == 4:
        Game.comp = "Spock"
        messagebox.showinfo(
            "Same choice!",
            "EGUALITY!\n"
            + "Your Choice: Spock\n"
            + "\nSheldon's Choice: "
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )

    else:
        Game.comp = "Rock"
        Game.user_score += 1
        messagebox.showinfo(
            "Congratulation!",
            "YOU WIN!\nSpock vaporizes Rock \nYour Choice: Spock\n"
            + "\nSheldon's choice:"
            + Game.comp
            + "\nYour Score: "
            + str(Game.user_score)
            + "\nSheldon's Score: "
            + str(Game.sheldon_score),
        )


B1 = tkinter.Button(
    top, image=Game.caillou_tk, height="300", width="280", command=Rock
)
B2 = tkinter.Button(
    top, image=Game.feuille_tk, height="300", width="280", command=paper
)
B3 = tkinter.Button(
    top, image=Game.ciseaux_tk, height="300", width="280", command=scissors
)
B4 = tkinter.Button(
    top, image=Game.lizard_tk, height="300", width="280", command=lizard
)
B5 = tkinter.Button(
    top, image=Game.spock_tk, height="300", width="280", command=spock
)

B1.pack(side="left")
B2.pack(side="left")
B3.pack(side="left")
B4.pack(side="left")
B5.pack(side="left")

top.mainloop()
