import turtle
import colorsys

s = "F"
rep1 = "-F++G-"
rep2 = "+F--G+"
its = 14

for k in range(its):
    z = [(i,s[i]) for i in range(len(s)-1, -1, -1) if s[i]=='F' or s[i]=='G']
    #print(z)
    for i in z:
        s = s[:i[0]]+(rep1 if i[1]=='F' else rep2)+s[i[0]+1:]
    #print(s)


#draw
turtle.setworldcoordinates(-200, -500, 800, 500)
turtle.setup(0.8, 0.8)
wn = turtle.Screen()
wn.delay(0)
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.ht()
angle = 45
speed = 6
steps = s.count('F')+s.count('G')
stepsSoFar = 0
for i in s:
    if(i=='F' or i=='G'):
        stepsSoFar += 1
        n = (1.0*stepsSoFar)/steps;
        t.pencolor(colorsys.hsv_to_rgb(n, 0.9,0.5))
        t.forward(speed)
    elif(i=='+'):
        t.left(angle)
    elif(i=='-'):
        t.right(angle)

    
