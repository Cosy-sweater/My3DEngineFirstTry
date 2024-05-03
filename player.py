import pygame
import pygame as pg
from camera import PlayerCamera
from constants import *


class Player(PlayerCamera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        super().__init__(app, position, yaw, pitch)

