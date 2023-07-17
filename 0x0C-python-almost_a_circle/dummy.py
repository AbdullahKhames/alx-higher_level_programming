#!/usr/bin/python3
"""
mod
"""

import turtle
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


def draw(list_rectangles, list_squares):
    turtles = []
    for _ in range(len(list_rectangles) + len(list_squares)):
        t = turtle.Turtle()
        t.speed(1)
        t.penup()
        turtles.append(t)

    for t, r in zip(turtles[:len(list_rectangles)], list_rectangles):
        t.setposition(r.x, r.y)
        t.pendown()
        t.forward(r.width)
        t.left(90)
        t.forward(r.height)
        t.left(90)
        t.forward(r.width)
        t.left(90)
        t.forward(r.height)
        t.penup()
        t.hideturtle()  # Hide the turtle

    for t, s in zip(turtles[len(list_rectangles):], list_squares):
        t.setposition(s.x, s.y)
        t.pendown()
        for _ in range(4):
            t.forward(s.size)
            t.left(90)
        t.penup()
        t.hideturtle()  # Hide the turtle

    turtle.done()


if __name__ == '__main__':
    t1 = turtle.Turtle()

    rect = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    sq = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]
    # draw(rect, sq)
    Base.draw(rect, sq)