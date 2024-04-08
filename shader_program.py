import moderngl as mgl

from settings import *


class ShaderProgram:
    def __init__(self, app) -> None:
        self.app = app
        self.context: mgl.Context = self.app.context
        self.player = app.player

        self.quad = self.get_program(shader_name="quad")

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self) -> None:
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

    def update(self) -> None:
        self.quad['m_view'].write(self.player.m_view)

    def get_program(self, shader_name: str) -> mgl.Program:
        with open(f"shaders/{shader_name}.vert") as vert_file, open(f"shaders/{shader_name}.frag") as frag_file:
            vertex_shader = vert_file.read()
            fragment_shader = frag_file.read()

        program = self.context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
