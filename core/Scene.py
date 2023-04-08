from core.Camera import Camera
from core.EventManager import EventManager 

class Scene(object):
    def __init__(self):
        self.gameobjects = []
        self.attach_camera(Camera(800, 800))
        self.event_manager = EventManager(self)

    def attach_camera(self, camera):
        self.camera = camera
        self.camera._on_attach(self)

    def attach_gameobject(self, gameobject):
        self.gameobjects.append(gameobject)
        gameobject.scene = self
        if "_on_attach" in dir(gameobject): gameobject._on_attach()

    def start(self):
        if "_on_start" in dir(self): self._on_start()
        for gameobject in self.gameobjects: gameobject.start()
        self.event_manager.start()

    def update(self, delta_time):
        if "_on_update" in dir(self): self._on_update(delta_time)
        for gameobject in self.gameobjects: gameobject.update(delta_time)

    def fire_event(self, event):
        if "_on_event" in dir(self): self._on_event(event)
        for gameobject in self.gameobjects: gameobject.fire_event(event)

        
