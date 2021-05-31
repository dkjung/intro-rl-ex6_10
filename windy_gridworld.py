import random
from enum import Enum

import numpy as np


class Direction(Enum):
    """General Direction Enum"""

    pass


class NormalDirection(Direction):
    """Enum for a normal (4) Direction"""

    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)


class KingsDirection(Direction):
    """Enum for the King's (8) direction"""

    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)
    UPRIGHT = (-1, 1)
    UPLEFT = (-1, -1)
    DOWNRIGHT = (1, 1)
    DOWNLEFT = (1, -1)


class WindyGridworld:
    """The Game of WindyGridworld"""

    def __init__(self, start: tuple[int, int] = (4, 0), goal: tuple[int, int] = (4, 7), width: int = 10,
                 height: int = 7):
        self.start = start
        self.goal = goal
        self.width = width
        self.height = height
        self.wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

        self.cur = start
        self.complete = False

        self.dir_list = list(NormalDirection)
        random.seed()

    def reset(self):
        """make the state cur to be the start state"""
        self.cur = self.start
        self.complete = False

    def step(self, d: Direction) -> tuple[int, bool]:
        """do one step with direction"""
        dy, dx = d.value
        cy, cx = self.cur
        ny, nx = cy + dy, cx + dx
        ny -= self.wind[cx]
        ny = min(max(0, ny), self.height - 1)
        nx = min(max(0, nx), self.width - 1)
        self.cur = (ny, nx)
        if self.cur == self.goal:
            self.complete = True
        return -1, self.cur == self.goal


class KingsWindyGridworld(WindyGridworld):
    """Grid world with King's move"""

    def __init__(self):
        super().__init__()
        self.dir_list = list(KingsDirection)


class StochasticWindKWG(KingsWindyGridworld):
    """Stochastic Wind King's Windy Gridworld"""

    def step(self, d: Direction) -> tuple[int, bool]:
        dy, dx = d.value
        cy, cx = self.cur
        ny, nx = cy + dy, cx + dx
        ny -= self.wind[cx]
        ny += random.randrange(-1, 2)
        ny = min(max(0, ny), self.height - 1)
        nx = min(max(0, nx), self.width - 1)
        self.cur = (ny, nx)
        if self.cur == self.goal:
            self.complete = True
        return -1, self.cur == self.goal
