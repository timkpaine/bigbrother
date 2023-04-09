def _partial(watcher, ref):
    def _watcher_wrapper(obj, method, other_ref, call_args, call_kwargs):
        return watcher(obj, method, ref, call_args, call_kwargs)

    return _watcher_wrapper
