#!/usr/bin/python

from tkinter import *
from tkinter import Tk
from random import randint
import random
import time

counter = 0
counter1 = 0

maFenetre = Tk()
maFenetre.title("Pong Game")
maFenetre.iconbitmap("@logopong.xbm")
maFenetre.resizable(0, 0)
maFenetre.wm_attributes("-topmost", 1)

def init_canevas(maFenetre):
    canvas = Canvas(maFenetre, width=600, height=400, bd=0, highlightthickness=0)
    canvas.config(bg="black")
    canvas.pack()
    maFenetre.update()
    canvas.create_line(300, 0, 300, 400, fill="white")

    return canvas


class Ball:
    def __init__(self, canvas, color, paddle, paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 300, 250)
        starts = [-3, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 600

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3

    def score(self, valeur):
        global counter
        global counter1

        if valeur == True:
            a = self.canvas.create_text(
                250, 40, text=counter, font=('Arial', 30), fill="white")
            canvas.itemconfig(a, fill="black")
            counter += 1
            a = self.canvas.create_text(
                250, 40, text=counter, font=('Arial', 30), fill="white")
        if valeur == False:
            a = self.canvas.create_text(
                350, 40, text=counter1, font=('Arial', 30), fill="white")
            canvas.itemconfig(a, fill="black")
            counter1 += 1
            a = self.canvas.create_text(
                350, 40, text=counter1, font=('Arial', 30), fill="white")


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 150, 30, 250, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_left(self, evt):
        self.y = -3

    def turn_right(self, evt):
        self.y = 3


class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(570, 150, 600, 250, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_left(self, evt):
        self.y = 3

    def turn_right(self, evt):
        self.y = -3



img = PhotoImage(file="Play.gif")
check = 0


def joue_on():
    global check

    check = 1


def isGameOver():
    return counter == 2 or counter1 == 2


def game_loop(ball, paddle, paddle1, maFenetre):
    # maFenetre.attributes('-fullscreen', 1)
    counter = 0
    counter1 = 0
    while not isGameOver():
        ball.draw()
        paddle.draw()
        paddle1.draw()

        if isGameOver():
            if counter == 2:
                ball.x = 0
                ball.y = 0
                paddle.y = 0
                paddle1.y = 0
                canvas.create_text(
                    250, 200, text="Player 2 WIN", font=32, fill="red")
                canvas.create_text(
                    250, 215, text="Score: " + str(counter) + "-" + str(counter1), font=32, fill="red")

            if counter1 == 2:
                ball.x = 0
                ball.y = 0
                paddle.y = 0
                paddle1.y = 0
                canvas.create_text(
                    250,
                    200,
                    text="Player 1 WIN", font=32, fill="green"
                )
                canvas.create_text(
                    250,
                    215,
                    text="Score: " + str(counter) + "-" + str(counter1), font=32, fill="green")

        time.sleep(0.01)
        maFenetre.update_idletasks()
        maFenetre.update()
        if isGameOver():
            if counter == 2:
                print('Game is Over Player 2 WIN !')
            else:
                print('Game is Over Player 1 WIN !')
            check = 0
            counter = 0
            counter1 = 0
            # A retirer si tu veux enchainer les parties
        #    maFenetre.destroy()


canvas = init_canevas(maFenetre)

button = Button(
    canvas,
    width=600,
    height=400,
    image=img,
    bg='black',
    command=joue_on
)

button.pack()


def startBoard():
    while 1:
        if isGameOver():
            # il faut afficher la page avec le bouton pour lancer le jeu
            menu()
            print('coucou')
        else:
            # il faudra réinitialiser le board avant de faire un launchGame (pour la 2nde partie)
            if check == 1:
                button.destroy()
                launchGame()
        maFenetre.update()


def menu():
    print('MENNUU')
    button = Button(
        canvas,
        width=600,
        height=400,
        image=img,
        bg='black',
        command=joue_on
    )
    button.pack()
    while isGameOver():
        if check == 1:
            button.destroy()
            counter = 0
            counter1 = 0
            launchGame()
        maFenetre.update()



def launchGame():
    paddle = Paddle(canvas, "green")
    paddle1 = Paddle1(canvas, "red")
    ball = Ball(canvas, "orange", paddle, paddle1)
    while not isGameOver():
        counter = 0
        counter1 = 0
        button.destroy()
        game_loop(ball, paddle, paddle1, maFenetre)
        maFenetre.update()


startBoard()
