from OpenGL import GL
from ext import vertex
from ctypes import c_void_p


class Triangle:
    def __init__(self, debug: bool = False):
        self.vertex = vertex.Vertex(position=(
                -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                0.0, 0.5, 0.0, 0.0, 0.0, 1.0),
            vertex_count=3
        )

        self.vertex_count = self.vertex.vertex_count

        if debug:
            print(self.vertex)

        self.vao = GL.glGenVertexArrays(1)  # Vertex Array Object, vbo is attached to vao
        GL.glBindVertexArray(self.vao)

        self.vbo = GL.glGenBuffers(1)   # Vertex Buffer Object, 1 is the ID basically
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)

        # Static Draw: Write Once, Read Many
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertex.position.nbytes, self.vertex.position, GL.GL_STATIC_DRAW)

        # Define Attribs in the vbo
        GL.glEnableVertexAttribArray(0)     # Attrib 0: Position
        # Attribute #, # of parts?, Data Type, Normalize?, Stride # bytes to next data
        # Each number as 4 bytes of data, 4 * 6 = 24 bytes
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, c_void_p(0))

        GL.glEnableVertexAttribArray(1)     # Attrib 1: Color
        # For c_void_p: offset is 0 bytes, first color starts 3 bytes in, offset of 3 * 4 = 12 bytes
        GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, c_void_p(12))

        # All this allocates memory for this!

    def destroy(self):
        GL.glDeleteVertexArrays(1, (self.vao,))
        GL.glDeleteBuffers(1, (self.vbo,))
