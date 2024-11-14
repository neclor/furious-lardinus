import sys
from typing import Tuple
import math
import pygame

import game.objects.base_object as base_object
import game.objects.entities.player as player



pause: bool = False


objects: list[dict] = []
enemies: list[dict] = []



def enter() -> None:
    init()


def init() -> None:
    global pause, objects
    pause = False
    objects = []


def update() -> None:
    pass
