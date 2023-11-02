import pygame
from OpenGL import GL
from OpenGL.GL.shaders import compileShader, compileProgram
from ext import color
from shapes import triangle


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

        # Init OpenGL
        r, g, b, a = color.rgba(12, 12, 12, 255)

        GL.glClearColor(r, g, b, a)
        self.shaders = self.create_shader("shaders/vertex.glsl", "shaders/fragment.glsl")

        GL.glUseProgram(self.shaders)
        self.triangle = triangle.Triangle()

        self.mainloop()

    def create_shader(self, vertex_file_path, fragment_file_path):  # noqa
        with open(vertex_file_path, 'r') as f:
            vertex_script = f.readlines()

        with open(fragment_file_path, 'r') as f:
            fragment_script = f.readlines()

        shader = compileProgram(
            compileShader(vertex_script, GL.GL_VERTEX_SHADER),
            compileShader(fragment_script, GL.GL_FRAGMENT_SHADER)
        )

        return shader

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Refresh Screen
            GL.glClear(GL.GL_COLOR_BUFFER_BIT)
            GL.glUseProgram(self.shaders)
            GL.glBindVertexArray(self.triangle.vao)
            # Draw Mode; Could use lines or points, Point to start from; Vertex 0, # of Points to Draw
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.triangle.vertex_count)

            pygame.display.flip()

            self.clock.tick(60)

        self.quit()

    def quit(self):  # noqa
        self.triangle.destroy()
        GL.glDeleteProgram(self.shaders)
        pygame.quit()


if __name__ == '__main__':
    App()
