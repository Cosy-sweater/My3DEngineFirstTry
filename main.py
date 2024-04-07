import pygame
import moderngl as mgl
import pygame as pg

import sys
from typing import NoReturn

import shader_program
from settings import *
from shader_program import ShaderProgram


class VoxelEngine:
    def __init__(self) -> None:
        # Pre-definitions
        self.shader_program = None

        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(WIN_RES, flags=pygame.OPENGL | pg.DOUBLEBUF)
        self.context: mgl.Context = mgl.create_context()

        self.context.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.context.gc_mode = "auto"

        self.clock: pg.time.Clock = pg.time.Clock()
        self.delta_time: int = 0
        self.time: float = 0

        self.is_running: bool = True

        self.on_init()

    def on_init(self):
        self.shader_program: shader_program.ShaderProgram = ShaderProgram(self)

    def update(self) -> None:
        self.shader_program.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001

        pg.display.set_caption(f"{self.clock.get_fps(): .0f}")

    def render(self) -> None:
        self.context.clear(color=BG_COLOR)
        pg.display.flip()

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self) -> NoReturn:
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()

        pg.quit()
        sys.exit()


def main() -> None:
    app = VoxelEngine()
    app.run()


if __name__ == '__main__':
    main()
