from settings import *
from world_objects.chunk import Chunk

from main import VoxelEngine


class World:
    def __init__(self, app: VoxelEngine):
        self.app = app

        self.chunks: list[Chunk | None] = [None for _ in range(WORLD_VOL)]
        self.voxels = np.empty([WORLD_VOL, CHUNK_VOL], dtype='uint8')
        self.build_chunk()
        self.build_chunk_mesh()

    def build_chunk(self):
        for x in range(WORLD_W):
            for y in range(WORLD_H):
                for z in range(WORLD_D):
                    chunk = Chunk(self, position=(x, y, z))

                    chunk_index = x + WORLD_W * z + WORLD_AREA * y
                    self.chunks[chunk_index] = chunk

                    # storing chunk voxels separately from chunks
                    self.voxels[chunk_index] = chunk.build_voxels()

                    # getting pointer to voxels
                    chunk.voxels = self.voxels[chunk_index]

    def build_chunk_mesh(self):
        for chunk in self.chunks:
            chunk.build_mesh()

    def update(self):
        pass

    def render(self):
        for chunk in self.chunks:
            chunk.render()
