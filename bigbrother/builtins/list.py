from typing import Any, Callable, List


class _ObservedList(List):
    _watcher: Callable[["_ObservedList", str, Any], None]

    def __init__(self, list: List, watcher: Callable[["_ObservedList", str, Any], None]):
        super().__init__(list)
        object.__setattr__(self, "_watcher", watcher)

    def append(self, *args, **kwargs):
        self._watcher(self, "append", *args, **kwargs)
        return super().append(*args, **kwargs)

    def clear(self, *args, **kwargs):
        self._watcher(self, "clear", *args, **kwargs)
        return super().clear(*args, **kwargs)

    def extend(self, *args, **kwargs):
        self._watcher(self, "extend", *args, **kwargs)
        return super().extend(*args, **kwargs)

    def insert(self, *args, **kwargs):
        self._watcher(self, "insert", *args, **kwargs)
        return super().insert(*args, **kwargs)

    def pop(self, *args, **kwargs):
        self._watcher(self, "pop", *args, **kwargs)
        return super().pop(*args, **kwargs)

    def remove(self, *args, **kwargs):
        self._watcher(self, "remove", *args, **kwargs)
        return super().remove(*args, **kwargs)

    def sort(self, *args, **kwargs):
        self._watcher(self, "sort", *args, **kwargs)
        return super().sort(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        self._watcher(self, "setattr", *args, **kwargs)
        return super().__setattr__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        self._watcher(self, "setitem", *args, **kwargs)
        return super().__setitem__(*args, **kwargs)
