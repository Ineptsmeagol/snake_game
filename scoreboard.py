from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-0, 270)
        with open("data.txt") as file:
            s = int(file.read())
            self.high_score = s
        self.show_scoreboard()

    def show_scoreboard(self):
        """Method to display the scoreboard at the top of the screen"""
        self.clear()
        new_score = f"Score: {self.score} High Score: {self.high_score}"
        self.write(new_score, align="center", font=("courier", 12, "bold"))

    def update_score(self):
        """Update the Score by 1 and refresh"""
        self.score += 1
        self.show_scoreboard()

    def reset(self):
        """Restart the game"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.show_scoreboard()

