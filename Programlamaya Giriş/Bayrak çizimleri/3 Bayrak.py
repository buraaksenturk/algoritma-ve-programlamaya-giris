import turtle
import random
ybs=turtle.Turtle()
ybs.speed(0)
def b1():
    for i in range(1):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        ybs.pu()
        ybs.goto(x, y)
        ybs.pd
        ybs.begin_fill()
        ybs.color("green")
        ybs.fd(315)
        ybs.left(90)
        ybs.fd(70)
        ybs.left(90)
        ybs.fd(315)
        ybs.end_fill()
        ybs.begin_fill()
        ybs.color("white")
        ybs.right(90)
        ybs.fd(70)
        ybs.right(90)
        ybs.fd(315)
        ybs.right(90)
        ybs.fd(70)
        ybs.end_fill()
        ybs.pu()
        ybs.right(180)
        ybs.fd(70)
        ybs.pd()
        ybs.begin_fill()
        ybs.color("blue")
        ybs.fd(70)
        ybs.left(90)
        ybs.fd(315)
        ybs.left(90)
        ybs.fd(70)
        ybs.end_fill()

def b2():
    for i in range(1):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        ybs.pu()
        ybs.goto(x,y)
        ybs.pd
        ybs.begin_fill()
        ybs.color("blue")
        ybs.fd(315)
        ybs.left(90)
        ybs.fd(70)
        ybs.left(90)
        ybs.fd(315)
        ybs.end_fill()
        ybs.begin_fill()
        ybs.color("blue")
        ybs.right(90)
        ybs.fd(70)
        ybs.right(90)
        ybs.fd(315)
        ybs.right(90)
        ybs.fd(70)
        ybs.end_fill()
        ybs.pu()
        ybs.right(180)
        ybs.fd(70)
        ybs.pd()
        ybs.begin_fill()
        ybs.color("blue")
        ybs.fd(70)
        ybs.left(90)
        ybs.fd(315)
        ybs.left(90)
        ybs.fd(70)
        ybs.end_fill()
        ybs.pu()
        ybs.left(90)
        ybs.fd(90)
        ybs.pd()
        ybs.begin_fill()
        ybs.color("white")
        ybs.pu()
        ybs.right(90)
        ybs.fd(25)
        ybs.left(90)
        ybs.pd()
        ybs.fd(50)
        ybs.left(80)
        ybs.fd(48)
        ybs.right(150)
        ybs.fd(50)
        ybs.left(70)
        ybs.fd(53)
        ybs.right(150)
        ybs.fd(52)
        ybs.left(80)
        ybs.fd(50)
        ybs.right(150)
        ybs.fd(50)
        ybs.left(75)
        ybs.fd(53)
        ybs.right(140)
        ybs.fd(50)
        ybs.left(70)
        ybs.fd(40)
        ybs.end_fill()
        

def b3():
    ybs.begin_fill()
    ybs.pencolor("black")
    ybs.pensize(1)
    for i in range(2):
        ybs.fd(40)
        ybs.left(90)
        ybs.fd(100)
        ybs.left(90)
    ybs.color("white")
    ybs.end_fill()
    
    ybs.pu()
    ybs.fd(40)
    ybs.pd()
    
    ybs.begin_fill()
    ybs.pencolor("dark green")
    for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(50)
        ybs.left(90)
    ybs.color("dark green")
    ybs.end_fill()
    
    ybs.left(90)
    ybs.fd(50)
    ybs.right(90)

    ybs.begin_fill()
    ybs.pencolor("red")
    for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(50)
        ybs.left(90)
    ybs.color("red")
    ybs.end_fill()  

def b4():
   ybs.begin_fill()
   ybs.pencolor("dark green")
   for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
   ybs.color("dark green")
   ybs.end_fill()
    
   ybs.left(90)
   ybs.fd(25)
   ybs.right(90)

   ybs.begin_fill()
   ybs.pencolor("yellow")
   for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
   ybs.color("yellow")
   ybs.end_fill()
   ybs.left(90)
   ybs.fd(25)
   ybs.right(90)


   ybs.begin_fill()
   ybs.pencolor("green")
   for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
   ybs.color("green")
   ybs.end_fill()

   ybs.right(90)
   ybs.fd(53)
   ybs.left(143)

   ybs.begin_fill()
   ybs.pencolor("red")
   ybs.fd(50)
   ybs.left(74)
   ybs.fd(50)
   ybs.left(143)
   ybs.fd(78)
   ybs.color("red")
   ybs.end_fill()
   ybs.left(90)

def b5():
    ybs.begin_fill()
    ybs.pencolor("black")
    for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
    ybs.color("black")
    ybs.end_fill()
    
    ybs.left(90)
    ybs.fd(25)
    ybs.right(90)

    ybs.begin_fill()
    ybs.pencolor("white")
    for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
    ybs.color("white")
    ybs.end_fill()

    ybs.left(90)
    ybs.fd(25)
    ybs.right(90)


    ybs.begin_fill()
    ybs.pencolor("red")
    for i in range(2):
        ybs.fd(100)
        ybs.left(90)
        ybs.fd(25)
        ybs.left(90)
    ybs.color("red")
    ybs.end_fill()

    ybs.right(90)
    ybs.fd(53)
    ybs.left(143)

    ybs.begin_fill()
    ybs.pencolor("green")
    ybs.fd(50)
    ybs.left(74)
    ybs.fd(50)
    ybs.left(143)
    ybs.fd(78)
    ybs.color("green")
    ybs.end_fill()
    ybs.left(90)

bayraklar=[b1,b2,b3,b4,b5]
for i in range(30):
    ekranx = random.randrange(-300, 300)
    ekrany = random.randrange(-300, 300)
    ybs.pu()
    ybs.goto(ekranx,ekrany)
    ybs.pd
    ciz=random.choice(bayraklar)
    ciz()


