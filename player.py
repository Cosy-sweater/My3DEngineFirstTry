import pygame as pg

from camera import SpectatorCamera as Camera
from settings import *
from main import VoxelEngine


class Player(Camera):
    def __init__(self, app: VoxelEngine, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

        self.is_following_mouse = True

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        for event in self.app.events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.is_following_mouse = False
                    pg.event.set_grab(False)
                    pg.mouse.set_visible(True)
                if event.button == 1:
                    self.is_following_mouse = True
                    pg.event.set_grab(True)
                    pg.mouse.set_visible(False)
        if self.is_following_mouse:
            if mouse_dx:
                self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSETIVITY)
            if mouse_dy:
                self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSETIVITY)

    def keyboard_control(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time
        if key_state[pg.K_w]:
            self.move_forward(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_SPACE]:
            self.move_up(vel)
        if key_state[pg.K_LSHIFT]:
            self.move_down(vel)
