from bigbrother import watch


def create_tester(instance, method_name, expected_args, expected_kwargs):
    called = []

    def track_changes(obj, method, *args, **kwargs):
        called.append(True)
        print(f"method: {method} args: {args} kwargs: {kwargs}")
        assert obj == instance
        assert method == method_name
        assert args == expected_args
        assert kwargs == expected_kwargs

    return watch(instance, track_changes), called
