#ElaineMack
#10-17-2026
#P4Lab1_MackElaine.py
#Use turtle and loops to draw a square and a triangle


import turtle

def draw_house(square_size):
    # Setup screen
    screen = turtle.Screen()
    screen.title("Square and Triangle House")
    
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)

    # 1. Draw the Square Base
    t.penup()
    t.goto(-square_size / 2, -square_size / 2) # Center the house base
    t.pendown()
    
    t.color("blue", "lightblue")
    t.begin_fill()
    for _ in range(4):
        t.forward(square_size)
        t.left(90)
    t.end_fill()

    # Move turtle to the top-left corner of the square to start the roof
    t.penup()
    t.goto(-square_size / 2, square_size / 2)
    t.pendown()

    # 2. Draw the Equilateral Triangle Roof
    t.color("red", "lightcoral")
    t.begin_fill()
    t.left(60)                  # Turn up to start the triangle slope
    t.forward(square_size)      # Left roof slope
    t.right(120)                # Apex turn
    t.forward(square_size)      # Right roof slope
    t.end_fill()

    # Hide turtle and keep window open
    t.hideturtle()
    screen.mainloop()

# Run the program with a base size of 200 pixels
if __name__ == "__main__":
    draw_house(square_size=200)
