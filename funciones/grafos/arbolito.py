import turtle
t = turtle.Turtle()
t.left(90)
t.speed(500)

a:float = 90

def tree(i:float, a:float):
    if i < 10.0:
        return
    else:
        t.forward(i)
        t.left(a)
        tree(3.0*i/4.25, a)
        t.right(2*a)
        tree(3.0*i/4.25, a)
        t.left(a)
        t.backward(i)

tree(200, a)
turtle.done()
