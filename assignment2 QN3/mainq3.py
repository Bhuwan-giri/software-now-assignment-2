import turtle
import math
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.right(60)          # inward turnin of as per  reuired
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

def main():
    # User input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle setup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    # Center the drawing
    radius = length / (2 * math.tan(math.pi / sides))
    turtle.goto(-length / 2, radius / 2)
    turtle.pendown()

    # Draw pattern
    draw_polygon(sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
