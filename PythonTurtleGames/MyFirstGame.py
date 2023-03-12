import turtle, random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pacman")
screen.setup(width=600,height=600)

turtle.register_shape("pacman_gif.gif")

pacman = turtle.Turtle()
pacman.speed(0)
pacman.shape("pacman_gif.gif")
pacman.penup()

score = 0
yaziPuan = turtle.Turtle()
yaziPuan.speed(0)
yaziPuan.shape("square")
yaziPuan.color("white")
yaziPuan.penup()
yaziPuan.hideturtle()
yaziPuan.goto(-200,200)

yaziPuan.write("Puan: {}".format(score), align = "center", font = ("Copperplate", 24, "normal"))

speed = 1
hizPuan = turtle.Turtle()
hizPuan.speed(0)
hizPuan.shape("square")
hizPuan.color("white")
hizPuan.penup()
hizPuan.hideturtle()
hizPuan.goto(200,-200)

hizPuan.write("Hız: {}".format(speed), align = "center", font = ("Copperplate", 24, "normal"))

def solaDon():
    pacman.left(30)

def sagaDon():
    pacman.right(30)

def hiziArtir():
    global speed
    speed += 1
    hizPuan.clear()
    hizPuan.write("Hız: {}".format(speed), align = "center", font = ("Copperplate", 24, "normal"))

def hiziAzalt():
    global speed
    speed -= 1
    hizPuan.clear()

    hizPuan.write("Hız: {}".format(speed), align = "center", font = ("Copperplate", 24, "normal"))

screen.listen()
screen.onkey(solaDon,"Left")
screen.onkey(sagaDon,"Right")
screen.onkey(hiziArtir,"Up")
screen.onkey(hiziAzalt,"Down")
screen.tracer(2)

maxHedef = 5
hedefler = []
for i in range(maxHedef):
    hedefler.append(turtle.Turtle())
    hedefler[i].penup()
    hedefler[i].color("red")
    hedefler[i].shape("circle")
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300,300), random.randint(-300,300))

while True:
    pacman.forward(speed)
    

    if pacman.xcor() > 300 or pacman.xcor() < -300:
        pacman.right(180)
    if pacman.ycor() > 300 or pacman.ycor() < -300:
        pacman.left(180)
    
    for i in range(maxHedef):
        hedefler[i].forward(1)
        if hedefler[i].xcor() > 500 or hedefler[i].xcor() < -500:
            hedefler[i].right(random.randint(150,250))
        if hedefler[i].ycor() > 500 or hedefler[i].ycor() < -500:
            hedefler[i].right(random.randint(150,250))
        

        if pacman.distance(hedefler[i]) < 40:
            hedefler[i].setposition(random.randint(-300,300), random.randint(-300,300))
            hedefler[i].right(random.randint(0,360))
            score = score + 1
            yaziPuan.clear()
            yaziPuan.write("Puan: {}".format(score), align = "center", font = ("Copperplate", 24, "normal"))

