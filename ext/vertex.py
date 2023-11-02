import numpy as np


class Vertex:
    def __init__(self, position, color=None, texture_coords=None, normal=None, vertex_count=1):
        self.position = np.array(position, dtype=np.float32)
        self.color = np.array(color, dtype=np.float32) if color else None
        self.texture_coords = np.array(texture_coords, dtype=np.float32) if texture_coords else None
        self.normal = np.array(normal, dtype=np.float32) if normal else None
        self.vertex_count = vertex_count

    def __repr__(self):
        return (f"Vertex(position=list({len(self.position)} items), color={self.color}"
                f", texture_coords={self.texture_coords}"
                f", normal={self.normal}")

    def __eq__(self, other):
        return self == other
