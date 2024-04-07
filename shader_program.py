import moderngl as mgl

from settings import *


class ShaderProgram:
    def __init__(self, app) -> None:
        self.app = app
        self.context: mgl.Context = self.app.context

        self.quad = self.get_program(shader_name="quad")

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self) -> None:
        pass

    def update(self) -> None:
        pass

    def get_program(self, shader_name: str) -> mgl.Program:
        with open(f"shaders/{shader_name}.vert") as vert_file, open(f"shaders/{shader_name}.frag") as frag_file:
            vertex_shader = vert_file.read()
            fragment_shader = frag_file.read()

        program = self.context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
