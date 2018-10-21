from itertools import dropwhile
from random import choice
from string import ascii_uppercase as letters, digits


class Robot:

    used_names = set()

    def __init__(self):
        self.reset()

    @staticmethod
    def new_names():
        while True:
            robo_names = [letters] * 2 + [digits] * 3
            yield "".join(choice(robo_name) for robo_name in robo_names)

    def rand_name(self):
        def used_name(name): return name in self.used_names
        names = self.new_names()
        return next(dropwhile(used_name, names))

    def reset(self):
        self.name = self.rand_name()
        self.used_names.add(self.name)