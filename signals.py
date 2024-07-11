from main import VoxelEngine
from constants import *


class Signal:
    def __init__(self):
        self.args = ()

    def execute(self, app: VoxelEngine):
        pass


class WorldBlockPlaced(Signal):
    def __init__(self, position: tuple[int, int, int], block_id: int):
        self.position, self.block_id = position, block_id

    def execute(self, app: VoxelEngine):
        from terrain_gen import set_voxel_id, get_index
        # app.scene.world.voxel_handler.set_voxel(pos=self.position, block_id=self.block_id)

        x, y, z = self.position
        chunk_index = x + WORLD_W * z + WORLD_AREA * y
        chunk = app.scene.world.chunks[chunk_index]

        chunk.voxels[get_index(x % CHUNK_SIZE, y % CHUNK_SIZE, z % CHUNK_SIZE)] = self.block_id
        chunk.mesh.rebuild()

        if chunk.is_empty:
            chunk.is_empty = False


class WorldBlockRemoved(WorldBlockPlaced):
    def __init__(self, position: tuple[int, int, int]):
        super().__init__(position, 0)

    def execute(self, app: VoxelEngine):
        super().execute(app)

        # adjacent chunk mesh rebuild call
        ...


class PlayerBlockPlaced(Signal):
    def execute(self, app: VoxelEngine):
        app.scene.world.voxel_handler.place_voxel()


class PlayerBlockRemoved(Signal):
    def execute(self, app: VoxelEngine):
        app.scene.world.voxel_handler.remove_voxel()
