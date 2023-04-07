# bigbrother
An evil, awful, terrible, no-good library for watching objects for mutation. Do not use this library.

[![Build Status](https://github.com/timkpaine/bigbrother/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/timkpaine/bigbrother/actions?query=workflow%3A%22Build+Status%22)
[![Coverage](https://codecov.io/gh/timkpaine/bigbrother/branch/main/graph/badge.svg)](https://codecov.io/gh/timkpaine/bigbrother)
[![License](https://img.shields.io/github/license/timkpaine/bigbrother)](https://github.com/timkpaine/bigbrother)
[![PyPI](https://img.shields.io/pypi/v/bigbrother.svg)](https://pypi.python.org/pypi/bigbrother)

## Overview
`bigbrother` is a mutation observer library. You can use it to watch your objects for changes. When your object changes, `bigbrother` will trigger your choice of callback. 


```python
x = {1: "a", 2: "b", 3: "c"}

def track_changes(obj, method, *args, **kwargs):
    print(f"method: {method}, args: {args}, kwargs: {kwargs}")

x = watch(x, track_changes)

x[1] = "x"

# prints: method: setitem, args: (1, 'x'), kwargs: {}
```

`bigbrother` can also embed itself recursively in your object by passing in argument `deepstate=True`.


## Supported types

### Builtins
Most builtin types are read-only and cannot have their method structure mutated, so we observe via replacement with thin wrappers. 

- `list` via `_ObservedList`
    - `append`
    - `clear`
    - `extend`
    - `insert`
    - `pop`
    - `remove`
    - `sort`
    - `__setattr__`
    - `__setitem__`
- `dict` via `_ObservedDict`
    - `clear`
    - `pop`
    - `popitem`
    - `update`
    - `__setattr__`
    - `__setitem__`
- `set` via `_ObservedSet`
    - `add`
    - `clear`
    - `difference_update`
    - `discard`
    - `intersection_update`
    - `pop`
    - `remove`
    - `symmetric_difference_update`
    - `update`
    - `__setattr__`


### Libraries
- `pydantic.BaseModel`
