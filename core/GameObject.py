from core.Math import Transform

class GameObject:
    def __init__(self):
        self.components = []
        self.transform = Transform()

    def attach_component(self, component):
        self.components.append(component)
        component.gameobject = self
        component.scene = self.scene
        component.attach()

    def start(self):
        if "_on_start" in dir(self): self._on_start()
        for component in self.components: component.start()

    def update(self, delta_time):
        if "_on_update" in dir(self): self._on_update(delta_time)
        for component in self.components: component.update(delta_time)

    def fire_event(self, event):
        if "_on_event" in dir(self): self._on_event(event)
        for component in self.components: component.fire_event(event)
