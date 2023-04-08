class SpriteRenderer:
    def __init__(self):
        self.sprites = []

    def add_sprite(self, sprite):
        sprite.window = self.camera.window
        self.sprites.append(sprite)

    def render(self):
        for sprite in sorted(self.sprites, key=lambda sprite: sprite.index): 
            sprite.render()
