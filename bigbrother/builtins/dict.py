from typing import Any, Callable, Dict


class _ObservedDict(Dict):
    _watcher: Callable[["_ObservedDict", str, Any], None]

    def __init__(self, dict: Dict, watcher: Callable[["_ObservedDict", str, Any], None]):
        super().__init__(dict)
        object.__setattr__(self, "_watcher", watcher)

    def clear(self, *args, **kwargs):
        self._watcher(self, "clear", *args, **kwargs)
        return super().clear(*args, **kwargs)

    def pop(self, *args, **kwargs):
        self._watcher(self, "pop", *args, **kwargs)
        return super().pop(*args, **kwargs)

    def popitem(self, *args, **kwargs):
        self._watcher(self, "popitem", *args, **kwargs)
        return super().popitem(*args, **kwargs)

    def update(self, *args, **kwargs):
        self._watcher(self, "update", *args, **kwargs)
        return super().update(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        self._watcher(self, "setattr", *args, **kwargs)
        return super().__setattr__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        self._watcher(self, "setitem", *args, **kwargs)
        return super().__setitem__(*args, **kwargs)
