from turtle import *
pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    end_fill()
    lt(25)
mainloop()