__version__ = "0.1.0"

from types import MethodType
from typing import Any, Callable, Dict, List, Set, TypeVar

from .generic import _replacement_setattr, _replacement_setitem
from .builtins import _ObservedDict, _ObservedList, _ObservedSet
from .libraries import _Pydantic__setattr__


try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = None


T = TypeVar("T")


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
    if BaseModel and isinstance(obj, BaseModel):
        # replace model's setattr
        setattr(obj, "__setattr__", MethodType(_Pydantic__setattr__(watcher=watcher), obj))

        # TODO recursively replace types

    # Others
    if hasattr(obj, "__setitem__"):
        setattr(obj, "__setitem__", MethodType(_replacement_setitem, obj))
    if hasattr(obj, "__setattr__"):
        setattr(obj, "__setattr__", MethodType(_replacement_setattr, obj))
    return obj


def watch(obj: T, watcher: Callable[[T, str, Any], None]) -> T:
    return _install_watcher(obj, watcher)
