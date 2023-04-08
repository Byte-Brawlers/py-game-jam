import pygame
from core.Component import Component

class Sprite(Component):
    def __init__(self, path_to_image = "./assets/default_sprite.png"):
        self.index = 0
        self.path_to_image = path_to_image

    def _on_attach(self):
        self.image = pygame.image.load(self.path_to_image).convert()
        self.rect = self.image.get_rect()
        self.scene.camera.sprite_renderer.add_sprite(self)

    def _on_update(self, delta_time):
        self.image = pygame.transform.scale(self.image, (400, 400))

    def _on_start(self):
        pass

    def render(self):
        self.window.blit(self.image, self.gameobject.transform.position.to_tuple())

