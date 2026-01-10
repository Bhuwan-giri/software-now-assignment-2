import turtle
def draw_pattern(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3

        draw_pattern(length, depth - 1)
        turtle.left(60)

        draw_pattern(length, depth - 1)
        turtle.right(120)

        draw_pattern(length, depth - 1)
        turtle.left(60)

        draw_pattern(length, depth - 1)

def main():
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 2)
    turtle.pendown()

    angle = 360 / sides

    for _ in range(sides):
        draw_pattern(side_length, depth)
        turtle.right(angle)

    turtle.done()

main()
