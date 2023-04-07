from core.Scene import Scene
from core.GameObject import GameObject

class MainScene(Scene):
    def _on_update(self):
        print("UPDATING Scene")

class Player(GameObject):
    def _on_attach(self):
        print("Player Attached")

    def _on_start(self):
        print("Game Started")

    def _on_update(self):
        print("Player Updating")

scene = MainScene()
scene.attach_gameobject(Player())
scene.start()

