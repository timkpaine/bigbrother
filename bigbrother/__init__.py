__version__ = "0.1.1"

from types import MethodType
from typing import Any, Callable, Dict, List, Set, TypeVar

from .generic import _replacement_setattr, _replacement_setitem
from .builtins import _ObservedDict, _ObservedList, _ObservedSet


try:
    from pydantic import BaseModel

except ImportError:
    BaseModel = None


T = TypeVar("T")


def _partial(watcher, obj):
    def _watcher_wrapper(*args, **kwargs):
        if args:
            args = args[1:]
        if kwargs:
            kwargs.pop("obj", None)
            kwargs.pop("self", None)
        return watcher(obj, *args, **kwargs)

    return _watcher_wrapper


def _install_watcher(obj: T, watcher: Callable[[T, str, Any], None]) -> T:
    # Standard mutable types
    if isinstance(obj, List):
        # can't mutate list so replace with watcher variant
        return _ObservedList(obj, watcher)

    if isinstance(obj, Set):
        return _ObservedSet(obj, watcher)

    if isinstance(obj, Dict):
        return _ObservedDict(obj, watcher)

    # Library types
    # Pydantic object
    if BaseModel and isinstance(obj, BaseModel):
        # iterate through fields doing the same
        for key, value in obj.__dict__.items():
            # TODO is this good enough?
            if isinstance(value, BaseModel):
                obj.__dict__[key] = _install_watcher(value, watcher)

        # replace dict with watched version
        object.__setattr__(obj, "__dict__", _install_watcher(obj.__dict__, _partial(watcher, obj)))
        return obj

    # Pydantic class
    # TODO

    # Others
    if hasattr(obj, "__setitem__"):
        setattr(obj, "__setitem__", MethodType(_replacement_setitem, obj))
    if hasattr(obj, "__setattr__"):
        setattr(obj, "__setattr__", MethodType(_replacement_setattr, obj))
    return obj


def watch(obj: T, watcher: Callable[[T, str, Any], None]) -> T:
    return _install_watcher(obj, watcher)


__all__ = ["watch", "__version__"]
