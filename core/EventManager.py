import pygame 

class EventManager:
    def __init__(self, scene):
        self.scene = scene

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    if "_on_quit" in dir(self.scene): self.scene._on_quit()
                self.scene.fire_event(event)
                self.scene.update()
        pygame.quit()


