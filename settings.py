from numba import njit
import numpy as np
import glm
import math

# window resolution
WIN_RES = glm.vec2(1600, 900)

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(0.5 * V_FOV) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSETIVITY = 0.002

# color presets
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)