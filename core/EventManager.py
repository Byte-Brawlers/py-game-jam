import pygame 
import time

class EventManager:
    def __init__(self, scene):
        self.scene = scene

    def start(self):
        self.running = True
        time_past = time.time()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    if "_on_quit" in dir(self.scene): self.scene._on_quit()
                self.scene.fire_event(event)
                time_now = time.time()
                self.scene.update(time_now - time_past)
                time_past = time_now

                self.scene.camera.display()

        pygame.quit()


