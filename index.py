import turtle

zero=[(0,0),(0,-40),(20,-40),(20,0),(0,0)]
one=[(0,-20),(20,0),(20,-40)]
two=[(0,0),(20,0),(20,-20),(0,-40),(20-40)]
three=[(0,0),(20,0),(0,-20),(20,-20),(0,-40)]
four=[(0,0),(0,-20),(20,-20),(20,0),(20,-40)]
five=[(20,0),(0,0),(0,-20),(20,-20),(20,-40),(0,-40)]
six=[(20,0),(0,-20),(0,-40),(20,-40),(20,-20),(0,-20)]
seven=[(0,0),(20,0),(0,-20),(0,-40)]
eight=[(0,0),(20,0),(20,-40),(0,-40),(0,0),(0,-20),(20,-20)]
nine=[(0,-40),(20,-20),(20,0),(0,0),(0,-20),(20,-20)]
cifr=[zero,one,two,three,four,five,six,seven,eight,nine]
ind=input()
for s in range (61):
    turtle.penup() 
    turtle.goto(s*40,0)
    c=int(ind[s])
    a,b=cifr[c][0]
    turtle.goto(s*40+a,0+b)
    turtle.pendown()
    for w in cifr[c]:
        a,b=w
        turtle.goto(s*40+a,b)
turtle.left(230)