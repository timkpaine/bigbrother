def _partial(watcher, obj):
    def _watcher_wrapper(*args, **kwargs):
        if args:
            args = args[1:]
        if kwargs:
            kwargs.pop("obj", None)
            kwargs.pop("self", None)
        return watcher(obj, *args, **kwargs)

    return _watcher_wrapper
