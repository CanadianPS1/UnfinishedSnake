import tkinter as tk
import keyboard
import random as r
import json
import os
from tkinter import *
window = tk.Tk()
window.geometry("1700x1020")
window.title("SNAKE")
currentMove = ""
snakeX = 50
snakeY = 500
speed = 5
appleX = 500
appleY = 500
border = Frame (window, bg="maroon",width=1700,height=1020)
gameField = Frame (window, bg="darkGreen",width=1640,height=960,takefocus=True)
gameField.place(x=30,y=40)
border.place(x=0,y=0)
global snakeAlive
snakeAlive = True
apple = Label(bg="red",width=3,height=1)
apple.place(x=appleX, y=appleY)
snake = Label(bg="lightgreen",width=6,height=3)
snake.pack()
snake.place(x = snakeX,y = snakeY)
score = 0
scoreLabel = Label(text= str(score), bg= "maroon", font=("Arial",16,"bold"))
scoreLabel.pack()
scoreLabel.place(x=850,y=0)
def gameLoop():
    global snakeX, snakeY
    global speed
    global currentMove
    #checks if the key pressed is one of the movment ones
    if(keyboard.is_pressed("w")):
        currentMove = "w"
    if(keyboard.is_pressed("s")):
        currentMove = "s"        
    if(keyboard.is_pressed("a")):
        currentMove = "a"
    if(keyboard.is_pressed("d")):
        currentMove = "d"
    #checks if you changed derection
    if(currentMove == "w"):
        snakeY -= speed
        snake.place(x = snakeX, y = snakeY)
    if(currentMove == "s"):
        snakeY += speed
        snake.place(x = snakeX, y = snakeY)
    if(currentMove == "a"):
        snakeX -= speed
        snake.place(x = snakeX, y = snakeY)
    if(currentMove == "d"):
        snakeX += speed
        snake.place(x = snakeX, y = snakeY)
    snakeAlive = detectEdge()
    detectApple()
    if snakeAlive:
        window.after(25, gameLoop)
    else:
        filePath = r"Python Code\JSON folder stuff\PythonSnakeHighScore.json"
        if os.path.exists(filePath):
            with open(filePath, "r") as file:
                infomation = json.load(file)
        else:
            infomation = {"HighScore": 0}
        if(infomation["HighScore"] < score):
            infomation["HighScore"] = score
            with open(filePath, "w") as file:
                    json.dump(infomation,file,indent=4)
        global highscore
        highscore = Label(text="HighScore: " + str(infomation["HighScore"]), font=("Helvetica", 40, "bold"), bg="darkGreen", height=2)
        highscore.pack(anchor="center", ipady=20, pady=50)
        global restartButton
        restartButton = Button(window, text="Play Again", command=restartGame, font=("Helvetica", 40, "bold"))
        restartButton.pack(anchor="center", ipady=20, pady=80)
def restartGame():
    global speed, appleX, appleY, snakeX, snakeY, snakeAlive, score, currentMove
    speed = 5
    appleX = 500
    appleY = 500
    snakeX = 50
    snakeY = 500
    score = 0
    scoreLabel.config(text= str(score))
    snakeAlive = True
    currentMove = ""
    restartButton.pack_forget()
    highscore.pack_forget()
    window.after(25, gameLoop)
#this detects the apple B)
def detectApple():
    global appleX, appleY, speed, score
    if abs(snakeX - appleX) < 50 and abs(snakeY - appleY) < 50:
        score += 1
        scoreLabel.config(text=str(score))
        speed += 1
        spawnApple()
def spawnApple():
    global appleX, appleY
    appleX = r.randint(30,1500)
    appleY = r.randint(40,900)
    apple.place(x = appleX, y= appleY)
#this detects the edge B)
def detectEdge():
    if(snakeX < 35):
        return False
    if(snakeX > 1615):
        return False
    if(snakeY < 45):
        return False
    if(snakeY > 945):
        return False
    return True
#calls the function B)
gameLoop()
#makes the frame and everything show up
window.mainloop()
