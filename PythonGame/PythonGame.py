from bangtal import *
import time
import random
import threading

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
setGameOption(GameOption.ROOM_TITLE, False)

background = Scene('0', 'Images/배경.jpg')

startbutton = Object('Images/start.png')
startbutton.locate(background, 300, 300)
startbutton.show()

heart1 = Object('Images/heart.png')
heart1.setScale(0.1)
heart1.locate(background, 1000, 650)

heart2 = Object('Images/heart.png')
heart2.setScale(0.1)
heart2.locate(background, 1100, 650)

heart3 = Object('Images/heart.png')
heart3.setScale(0.1)
heart3.locate(background, 1200, 650)

gameover = Object('Images/gameover.png')
gameover.locate(background, 300, 300)

life = 3

score = 0

timer = 0

target = Object('Images/target.png')
target.clicked = 1
target.setScale(0.1)

def Time_late():
    timer.cancel()
    Game_Start()

def Time_check():
    global timer
    timer = threading.Timer(0.7, Time_late)
    timer.start()

def Game_End():
    global score
    target.hide()
    gameover.show()
    print('당신의 점수는', score, '점입니다!')
    time.sleep(3)
    endGame()
   

def Game_Start():
    global life
    if not target.clicked:
        if life == 3:
            heart3.hide()
            life -= 1
        elif life == 2:
            heart2.hide()
            life -= 1
        else:
            heart1.hide()
            life -= 1
            Game_End()
            return;

    target.clicked = 0
    
    randomx = random.randrange(100, 1201)
    randomy = random.randrange(0, 400)
    target.locate(background, randomx, randomy)
    target.show()
    Time_check()


def startbutton_onMouseAction(x, y, Action):
    startbutton.hide()
    heart1.show()
    heart2.show()
    heart3.show()
    Game_Start()
startbutton.onMouseAction = startbutton_onMouseAction

def target_onMouseAction(x, y, Action):
    global score
    target.clicked = 1
    score += 100
    timer.cancel()
    Game_Start()
target.onMouseAction = target_onMouseAction

startGame(background)