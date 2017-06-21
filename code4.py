import math
import turtle
bob=turtle.Turtle()
print(bob)

for i in range(4):
    bob.fd(200)
    bob.lt(90)

import turtle
bob=turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob,100)

def polygon(t,n,length):
    angle=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob,7,100)

def circle(t,r):
    circumference=2*math.pi*r
    n=10
    length=circumference/n
    polygon(t,n,length)

circle(bob,100)

def circle(t,r):
    circumference=2*math.pi*r
    n=20
    length=circumference/n
    polygon(t,n,length)

circle(bob,100)

def circle(t,r):
    circumference=2*math.pi*r
    n=50
    length=circumference/n
    polygon(t,n,length)

circle(bob,100)

def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+3
    length=circumference/n
    polygon(t,n,length)

circle(bob,100)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n

for i in range(5):
    t.fd(step_length)
    t.lt(step_angle)

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n,length):
    angle=360/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t,n,step_length, step_angle)

arc(bob,150,30)

turtle.mainloop()
