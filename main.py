import turtle
import random

FONT = ('Consolas', 30, 'normal')
game_over = False
Score = 0

Screen = turtle.Screen()
GameTimer = turtle.Turtle()
ScoreBoard = turtle.Turtle()
GameTurtle = turtle.Turtle()

top_height = Screen.window_height() / 2

Screen.bgcolor("light blue")
Screen.title("Game Screen")

x_cordinates = [90, 180, 0, -90, -180]
y_cordinates = [90, 180, 0, -90, -180]

def SetupScoreBoard():
    global top_height
    ScoreBoard.color("dark blue")
    ScoreBoard.hideturtle()
    ScoreBoard.penup()
    y = top_height * 0.85
    ScoreBoard.setpos(0, y)
    ScoreBoard.write(arg="Score:0", move=False, align='center', font=FONT)

def SetupGameTurtle():
    GameTurtle.color("black", "forest green")
    GameTurtle.shape("turtle")
    GameTurtle.shapesize(2, 2)

    def HandleClick(x, y):
        global Score
        Score += +1
        ScoreBoard.clear()
        ScoreBoard.write(arg=f"Score: {Score}", move=False, align='center', font=FONT)
    GameTurtle.onclick(HandleClick)

def TeleportingTurtles():
    if not game_over:
        GameTurtle.teleport(random.choice(x_cordinates), random.choice(y_cordinates))
        Screen.ontimer(TeleportingTurtles,800)
def Timer(time):
    global top_height
    global game_over
    GameTimer.color("dark blue")
    GameTimer.hideturtle()
    GameTimer.penup()
    y = top_height * 0.85
    GameTimer.setposition(11, y -30)

    if time > 0:
        GameTimer.clear()
        GameTimer.write(f"Time : {time}", move = False,align='center', font=FONT)
        Screen.ontimer(lambda: Timer(time - 1), 1000)
    else:
        game_over = True
        ScoreBoard.clear()
        GameTimer.clear()
        GameTurtle.clear()
        GameTurtle.hideturtle()
        ScoreBoard.write(f"TİME'S UP YOUR SCORE :{Score}", align='center', font=FONT)
def Game():
    turtle.tracer(0)
    SetupGameTurtle()
    SetupScoreBoard()
    TeleportingTurtles()
    Timer(20)
    turtle.tracer(1)

Game()
turtle.done()