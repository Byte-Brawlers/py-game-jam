class GameObject:
    def __init__(self):
        pass

    def start(self):
        if "_on_start" in dir(self): self._on_start()

    def update(self):
        if "_on_update" in dir(self): self._on_update()

    def fire_event(self, event):
        if "_on_event" in dir(self): self._on_event(event)
