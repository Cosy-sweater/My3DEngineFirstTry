from settings import *
from main import VoxelEngine


class Chunk:
    def __init__(self, app: VoxelEngine):
        self.app = app

        self.voxels: np.array = self.build_voxels()

    @staticmethod
    def build_voxels():
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                for y in range(CHUNK_SIZE):
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = 1
        return voxels
