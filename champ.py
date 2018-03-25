import turtle

def repeat_shape(sq):
    sq.speed(15)
    for i in range(1,5,1):
        sq.forward(100)
        sq.right(90)
    return

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('orange')
    brad = turtle.Turtle()
    brad.shape('arrow')
    brad.speed(15)
    for i in range(1,80,1):
        repeat_shape(brad)
        brad.right(5)
    return

draw_flower()
