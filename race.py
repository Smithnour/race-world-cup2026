import random

class Team:
    def __init__(self, name):
        self.name = name
        self.speed = random.randint(40, 80)
        self.distance = 0

    def move(self):
        self.distance += self.speed + random.randint(-5, 10)
