import colorgram   # package
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)    # 要多少顏色

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

circle = t.Turtle()
t.colormode(255)
circle.penup()
circle.hideturtle()


def row_spot():                      # 定義點的function
    for i in range(0, 10):
        circle.setx(50 * i - 225)
        circle.dot(20, color_list[random.randint(0, 27)])


for j in range(0, 10):               # 定義y軸
    circle.speed(0)
    circle.sety(50 * j - 225)
    row_spot()

screen = t.Screen()    #Screen() is a class, screen is a object
screen.exitonclick()   #exitonclick() is a method


