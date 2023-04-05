from pytest import fixture
from ..common import create_tester


@fixture
def a_dict():
    return {1: "a", 2: "b", 3: "c"}


class TestDict:
    def test_dict_clear(self, a_dict):
        instance, called = create_tester(a_dict, "clear", (), {})
        instance.clear()
        assert called[0]
        assert instance == {}

    def test_dict_pop(self, a_dict):
        instance, called = create_tester(a_dict, "pop", (1,), {})
        instance.pop(1)
        assert called[0]
        assert instance == {2: "b", 3: "c"}

    def test_dict_popitem(self, a_dict):
        instance, called = create_tester(a_dict, "popitem", (), {})
        instance.popitem()
        assert called[0]
        assert instance == {1: "a", 2: "b"}

    def test_dict_update(self, a_dict):
        instance, called = create_tester(a_dict, "update", ({4: "d"},), {})
        instance.update({4: "d"})
        assert called[0]
        assert instance == {1: "a", 2: "b", 3: "c", 4: "d"}

    def test_dict___setitem__(self, a_dict):
        instance, called = create_tester(a_dict, "setitem", (1, "x"), {})
        instance[1] = "x"
        assert called[0]
        assert instance == {1: "x", 2: "b", 3: "c"}
