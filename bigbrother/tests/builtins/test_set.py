from pytest import fixture
from ..common import create_tester


@fixture
def a_set():
    return {1, 2, 3}


class TestDict:
    def test_set_add(self, a_set):
        instance, called = create_tester(a_set, "add", (4,), {})
        instance.add(4)
        assert called[0]
        assert instance == {1, 2, 3, 4}

    def test_set_clear(self, a_set):
        instance, called = create_tester(a_set, "clear", (), {})
        instance.clear()
        assert called[0]
        assert instance == set()

    def test_set_difference_update(self, a_set):
        instance, called = create_tester(a_set, "difference_update", ({1, 2, 4},), {})
        instance.difference_update({1, 2, 4})
        assert called[0]
        assert instance == {3}

    def test_set_discard(self, a_set):
        instance, called = create_tester(a_set, "discard", (1,), {})
        instance.discard(1)
        assert called[0]
        assert instance == {2, 3}

    def test_set_intersection_update(self, a_set):
        instance, called = create_tester(a_set, "intersection_update", ({1, 3},), {})
        instance.intersection_update({1, 3})
        assert called[0]
        assert instance == {1, 3}

    def test_set_remove(self, a_set):
        instance, called = create_tester(a_set, "remove", (1,), {})
        instance.remove(1)
        assert called[0]
        assert instance == {2, 3}

    def test_set_symmetric_difference_update(self, a_set):
        instance, called = create_tester(a_set, "intersection_update", ({1, 3},), {})
        instance.intersection_update({1, 3})
        assert called[0]
        assert instance == {1, 3}

    def test_set_update(self, a_set):
        instance, called = create_tester(a_set, "update", ({4, 5},), {})
        instance.update({4, 5})
        assert called[0]
        assert instance == {1, 2, 3, 4, 5}
