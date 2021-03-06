class Factory:
    def __init__(self, command):
        self.command = command
        self._builders = {}
        for cmd in self.command.__subclasses__():
            name = str(cmd.__name__)
            self.register_builder(name, cmd)

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

    @property
    def builders(self):
        return self._builders




     



