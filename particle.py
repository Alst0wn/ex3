import turtle


x=0
y=100
vy=0
vx=10
dt=0.01
ay=-9.81
turtle.speed(10)
turtle.hideturtle()
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
for s in range (10000):
    x += vx*dt
    y += vy*dt + ay*dt**2/2
    vy += ay*dt
    if (y<0):
        vy=-vy
        y=0
    turtle.goto(x,y)