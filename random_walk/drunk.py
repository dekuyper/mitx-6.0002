import random


class Drunk(object):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self is None:
            return 'Anonymous'
        return self.name


class UsualDrunk(Drunk):
    @staticmethod
    def take_step():
        step_choices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):
    @staticmethod
    def take_step():
        step_choices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class EWDrunk(Drunk):
    @staticmethod
    def take_step():
        step_choices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)
