import turtle

s = "F"
rep1 = "-F++G-"
rep2 = "+F--G+"
its = 15

for k in range(its):
    z = [(i,s[i]) for i in range(len(s)-1, -1, -1) if s[i]=='F' or s[i]=='G']
    #print(z)
    for i in z:
        s = s[:i[0]]+(rep1 if i[1]=='F' else rep2)+s[i[0]+1:]
    #print(s)


#draw
turtle.setworldcoordinates(-500, -500, 500, 500)
wn = turtle.Screen()
wn.delay(1)
t = turtle.Turtle()
t.speed(0)
t.ht()
angle = 45
speed = 10
for i in s:
    if(i=='F' or i=='G'):
        t.forward(speed)
    elif(i=='+'):
        t.left(angle)
    elif(i=='-'):
        t.right(angle)

    
