import pygame 
from core.SpriteRenderer import SpriteRenderer

class Camera(object):
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.sprite_renderer = SpriteRenderer()
        self.sprite_renderer.camera = self

    def _on_attach(self, scene):
        self.scene = scene
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

    def clear(self):
        self.window.fill((250, 250, 250))

    def display(self):
        self.clear()
        self.sprite_renderer.render()
        pygame.display.update()


