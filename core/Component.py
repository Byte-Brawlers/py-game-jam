class Component:
    def __init__(self):
        pass

    def attach(self):
        if "_on_attach" in dir(self): self._on_attach()

    def start(self):
        if "_on_start" in dir(self): self._on_start()

    def update(self, delta_time):
        if "_on_update" in dir(self): self._on_update(delta_time)

    def fire_event(self, event):
        if "_on_event" in dir(self): self._on_event(event)
