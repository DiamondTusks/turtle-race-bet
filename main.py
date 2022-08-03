from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
race_is_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


screen.exitonclick()
