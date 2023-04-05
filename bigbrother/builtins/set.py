from typing import Any, Callable, Set


class _ObservedSet(Set):
    _watcher: Callable[["_ObservedSet", str, Any], None]

    def __init__(self, set: Set, watcher: Callable[["_ObservedSet", str, Any], None]):
        super().__init__(set)
        object.__setattr__(self, "_watcher", watcher)

    def add(self, *args, **kwargs):
        self._watcher(self, "add", *args, **kwargs)
        return super().add(*args, **kwargs)

    def clear(self, *args, **kwargs):
        self._watcher(self, "clear", *args, **kwargs)
        return super().clear(*args, **kwargs)

    def difference_update(self, *args, **kwargs):
        self._watcher(self, "difference_update", *args, **kwargs)
        return super().difference_update(*args, **kwargs)

    def discard(self, *args, **kwargs):
        self._watcher(self, "discard", *args, **kwargs)
        return super().discard(*args, **kwargs)

    def intersection_update(self, *args, **kwargs):
        self._watcher(self, "intersection_update", *args, **kwargs)
        return super().intersection_update(*args, **kwargs)

    def pop(self, *args, **kwargs):
        self._watcher(self, "pop", *args, **kwargs)
        return super().pop(*args, **kwargs)

    def remove(self, *args, **kwargs):
        self._watcher(self, "remove", *args, **kwargs)
        return super().remove(*args, **kwargs)

    def symmetric_difference_update(self, *args, **kwargs):
        self._watcher(self, "symmetric_difference_update", *args, **kwargs)
        return super().symmetric_difference_update(*args, **kwargs)

    def update(self, *args, **kwargs):
        self._watcher(self, "update", *args, **kwargs)
        return super().update(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        self._watcher(self, "setattr", *args, **kwargs)
        return super().__setattr__(*args, **kwargs)
