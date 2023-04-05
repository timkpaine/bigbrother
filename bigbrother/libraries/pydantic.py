def _Pydantic__setattr__(watcher):
    def __setattr__(self, name, value):
        watcher(name, value)
        super().__setattr__(name, value)

    return __setattr__
