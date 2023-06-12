from turtle import *
speed('fastest')
s= Screen()
s.setup(1000,700)
colors=['red','blue']
pencolor('green')
pensize(5)
for i in range(6,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()
