import turtle

def draw_drawing(shanu):
    for i in range(0,4,1):
        shanu.forward(100)
        shanu.right(90)
    shanu.right(5)
    return

def draw_flower():
    windows = turtle.Screen()
    windows.bgcolor("orange")
    srt = turtle.Turtle()
    srt.shape('turtle')
    srt.speed(20)
    for i in range(1,85,1):
        draw_drawing(srt)
    windows.exitOnClick()


draw_flower()
