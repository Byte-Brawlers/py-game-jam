import pygame 

class Camera(object):
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    def _on_attach(self, scene):
        self.scene = scene
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

    def clear(self):
        self.window.clear()

    def display(self):
        pygame.window.update()


