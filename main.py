import turtle
import random
import time

score = 0
t = 15
best = 0
a = 0
b = 0

#minigame1
minigame1 = turtle.Turtle()
minigame1.shape("square")
minigame1.penup()
turtle.tracer(0)
minigame1.goto(-150,50)
minigame1.write("Timed", font=("arial", 40))
minigame1.goto(-175,75)
turtle.tracer(1)


turtle.tracer(0)
ctc = turtle.Turtle()
ctc.penup()
ctc.hideturtle()
ctc.goto(-150,150)
ctc.write("Catch the Turtle", font=("arial", 40))


cturtle = turtle.Turtle()
cturtle.hideturtle()
cturtle.penup()
cturtle.goto(-350, -50)

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(200, 300)

game_board = turtle.Screen()
game_board.bgcolor("light green")
game_board.title("Catch the Turtle")

start = turtle.Turtle()
start.hideturtle()
start.penup()
start.goto(-350,0)

scoreboard_turtle = turtle.Turtle()
scoreboard_turtle.hideturtle()
scoreboard_turtle.penup()
scoreboard_turtle.goto(-400, 300)
scoreboard_turtle.color("Black")

bestscore = turtle.Turtle()
bestscore.hideturtle()
bestscore.penup()
bestscore.goto(-150,300)

target = turtle.Turtle()
target.shape("turtle")
target.color("dark green")
target.hideturtle()


turtle.tracer(1)

def startfunc(x,y):
    global a
    global b
    ctc.clear()
    bestscore.write("Best Score:0", font=("arial", 40))
    scoreboard_turtle.write("Score: 0", font=("arial", 40))
    start.write("Please Press Space", font=("arial", 50))
    timer.write("Time:15", font=("arial", 40))
    minigame1.clear()
    minigame1.hideturtle()
    game_board.onkey(fun=escapefunc, key="space")
    minigame2.clear()
    minigame2.hideturtle()
    cturtle.write("Press C for return menu", font=("arial", 40))
    game_board.onkey(fun=cfunc, key="c")
    b = 0
    a = 0


def escapefunc():
    global t
    global score
    global a
    global b
    b = 0
    if a == 0:
        t = 15
        score = 0
        start.clear()
        timer.clear()
        scoreboard_turtle.clear()
        scoreboard_turtle.write("Score: 0", font=("arial", 40))
        bestscore.clear()
        bestscore.write("Best Score:{}".format(best), font=("arial", 40))
        cturtle.clear()
        a = 1
        while b == 0:
            turtle.tracer(0)
            timer.write("Time:{}".format(t), font=("arial", 40))
            random_x = random.randint(-200, 200)
            random_y = random.randint(-200, 200)
            target.penup()
            target.hideturtle()
            target.goto(random_x, random_y)
            target.showturtle()
            target.pendown()
            time.sleep(1)
            t -= 1
            timer.clear()
            timer.write("Time:{}".format(t), font=("arial", 40))
            bestscore.clear()
            bestscore.write("Best Score:{}".format(best), font=("arial", 40))
            turtle.tracer(1)

            if t == 0:
                cturtle.write("Press C for return menu", font=("arial", 40))
                t = 15
                a = 0
                score = 0
                endgame()
                break

        if b == 1:
            turtle.tracer(0)
            scoreboard_turtle.clear()
            bestscore.clear()
            target.hideturtle()
            timer.clear()
            turtle.tracer(1)


def targetclickfunc(x, y):
    global score
    global best
    score += 1
    print("turtle was clicked")
    scoreboard_turtle.clear()
    scoreboard_turtle.write("Score: {}".format(score), font=("arial", 40))
    if score > best:
        best = score


def endgame():
    global t
    minigame2.clear()
    target.hideturtle()
    timer.clear()
    timer.write("Game Over", font=("arial", 40))
    start.write("Please Press Space", font=("arial", 50))

def cfunc():
    global a
    global b
    turtle.tracer(0)
    a = 1
    b = 1
    timer.clear()
    timerx.clear()
    scoreboard_turtle.clear()
    bestscore.clear()
    start.clear()
    sinfo.clear()
    tinfo.clear()
    sinfo.hideturtle()
    tinfo.hideturtle()
    cturtle.clear()
    targetx.hideturtle()
    targety.hideturtle()
    target.hideturtle()
    minigame1.showturtle()
    minigame1.goto(-150, 50)
    minigame1.write("Timed", font=("arial", 40))
    minigame1.goto(-175, 75)
    minigame2.showturtle()
    minigame2.goto(-150, -75)
    minigame2.write("Scored", font=("arial", 40))
    minigame2.goto(-175, -50)
    ctc.write("Catch the Turtle", font=("arial", 40))
    timer.clear()
    timerx.clear()
    scoreboard_turtle.clear()
    bestscore.clear()
    start.clear()
    sinfo.clear()
    tinfo.clear()
    sinfo.hideturtle()
    tinfo.hideturtle()
    cturtle.clear()
    targetx.hideturtle()
    targety.hideturtle()
    target.hideturtle()
    minigame1.showturtle()
    minigame1.goto(-150, 50)
    minigame1.write("Timed", font=("arial", 40))
    minigame1.goto(-175, 75)
    minigame2.showturtle()
    minigame2.goto(-150, -75)
    minigame2.write("Scored", font=("arial", 40))
    minigame2.goto(-175, -50)
    ctc.write("Catch the Turtle", font=("arial", 40))
    turtle.tracer(1)

game_board.listen()
target.onclick(targetclickfunc)
minigame1.onclick(startfunc)
game_board.onkey(fun=cfunc, key="c")

#minigame2

turtle.tracer(0)
minigame2 = turtle.Turtle()
minigame2.shape("square")
minigame2.penup()
minigame2.goto(-150, -75)
minigame2.write("Scored", font=("arial", 40))
minigame2.goto(-175, -50)
turtle.tracer(1)
scorex = 0
bestx = 0
tx = 5
turtle.tracer(0)
targetx = turtle.Turtle()
targetx.shape("turtle")
targetx.color("red")
targetx.hideturtle()

targety = turtle.Turtle()
targety.shape("turtle")
targety.color("purple")
targety.hideturtle()

tinfo = turtle.Turtle()
tinfo.shape("turtle")
tinfo.color("purple")

sinfo = turtle.Turtle()
sinfo.shape("turtle")
sinfo.color("red")

sinfo.hideturtle()
tinfo.hideturtle()
sinfo.penup()
tinfo.penup()
sinfo.goto(-350,-150)
tinfo.goto(-100, -150)
sinfo.shapesize(2)
tinfo.shapesize(2)

timerx = turtle.Turtle()
timerx.hideturtle()
timerx.penup()
timerx.goto(200, 300)
turtle.tracer(1)
def startfuncx(x,y):
    global a
    global b
    global t
    ctc.clear()
    bestscore.write("Best Score:0", font=("arial", 40))
    scoreboard_turtle.write("Score: 0", font=("arial", 40))
    start.write("Please Press Space", font=("arial", 50))
    timerx.write("Time:5", font=("arial", 40))
    minigame1.clear()
    minigame1.hideturtle()
    minigame2.clear()
    minigame2.hideturtle()
    game_board.onkey(fun=spacefuncx, key="space")
    sinfo.write(":+2P",font=("arial", 50))
    tinfo.write(":+3S",font=("arial", 50))
    sinfo.goto(-400, -125)
    tinfo.goto(-150, -125)
    sinfo.showturtle()
    tinfo.showturtle()
    cturtle.write("Press C for return menu", font=("arial", 40))
    game_board.onkey(fun=cfunc, key="c")
    b = 0
    a = 0

def targetclickfuncx(x, y):
    global scorex
    global bestx
    global tx
    scorex += 2
    print("turtle was clicked")
    scoreboard_turtle.clear()
    scoreboard_turtle.write("Score: {}".format(scorex), font=("arial", 40))
    if scorex > bestx:
        bestx = scorex
def targetclickfuncy(x, y):
    global scorex
    global bestx
    global tx
    tx += 3
    print("turtle was clicked")
def spacefuncx():
    global tx
    global scorex
    global a
    if a == 0:
        start.clear()
        timerx.clear()
        scoreboard_turtle.clear()
        scoreboard_turtle.write("Score: 0", font=("arial", 40))
        bestscore.clear()
        bestscore.write("Best Score:{}".format(bestx), font=("arial", 40))
        sinfo.clear()
        tinfo.clear()
        sinfo.hideturtle()
        tinfo.hideturtle()
        cturtle.clear()
        a = 1
        while b == 0:
            timerx.write("Time:{}".format(tx), font=("arial", 40))
            random_xx = random.randint(-200, 200)
            random_yx = random.randint(-200, 200)
            targetx.penup()
            targetx.hideturtle()
            targetx.goto(random_xx, random_yx)
            targetx.showturtle()
            random_xy = random.randint(-200, 200)
            random_yy = random.randint(-200, 200)
            targety.penup()
            targety.hideturtle()
            targety.goto(random_xy, random_yy)
            targety.showturtle()
            time.sleep(0.5)
            tx -= 1
            timerx.clear()
            timerx.write("Time:{}".format(tx), font=("arial", 40))
            bestscore.clear()
            bestscore.write("Best Score:{}".format(bestx), font=("arial", 40))
            if tx == 0:
                tx = 5
                a = 0
                cturtle.write("Press C for return menu", font=("arial", 40))
                scorex = 0
                endgamex()
                break
            if b == 1:
                turtle.tracer(0)
                scoreboard_turtle.clear()
                timerx.clear()
                bestscore.clear()
                targetx.hideturtle()
                targety.hideturtle()
                turtle.tracer(1)

def endgamex():
    global tx
    targetx.hideturtle()
    targety.hideturtle()
    minigame2.clear()
    minigame1.clear()
    timerx.clear()
    timerx.write("Game Over", font=("arial", 40))
    start.write("Please Press Space", font=("arial", 50))





minigame2.onclick(startfuncx)
targetx.onclick(targetclickfuncx)
targety.onclick(targetclickfuncy)


turtle.mainloop()
