from core.Scene import Scene
from core.GameObject import GameObject
from components.Sprite import Sprite

class MainScene(Scene):
    def _on_update(self, delta_time):
        pass

class Player(GameObject):
    def _on_attach(self):
        self.attach_component(Sprite("./assets/default_sprite.png"))

    def _on_start(self):
        pass

    def _on_update(self, delta_time):
        pass

scene = MainScene()
scene.attach_gameobject(Player())
scene.start()



