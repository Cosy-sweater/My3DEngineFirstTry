from settings import *
from meshes.quad_mesh import QuadMesh
from main import VoxelEngine


class Scene:
    def __init__(self, app: VoxelEngine):
        self.app = app
        self.quad = QuadMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.quad.render()
