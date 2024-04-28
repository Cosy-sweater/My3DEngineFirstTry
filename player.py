import pygame
import pygame as pg
from camera import SpectatorCamera as Camera
from settings import *


class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

        self.lock_mouse = False

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def handle_event(self, event):
        # adding and removing voxels with clicks
        if event.type == pg.MOUSEBUTTONDOWN:
            voxel_handler = self.app.scene.world.voxel_handler
            if event.button == 3:
                voxel_handler.set_voxel()
            if event.button == 1:
                voxel_handler.remove_voxel()

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        for event in self.app.events:
            if event.type == pygame.KEYDOWN and event.key == pg.K_ESCAPE:
                self.lock_mouse = not self.lock_mouse
                pg.event.set_grab(self.lock_mouse)
                pg.mouse.set_visible(not self.lock_mouse)
        if self.lock_mouse:
            if mouse_dx:
                self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
            if mouse_dy:
                self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

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
