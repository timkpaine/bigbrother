from pytest import fixture
from ..common import create_tester


@fixture
def a_list():
    return [1, 2, 3]


class TestList:
    def test_list_append(self, a_list):
        instance, called = create_tester(a_list, "append", (1,), {})
        instance.append(1)
        assert called[0]
        assert instance == [1, 2, 3, 1]

    def test_list_clear(self, a_list):
        instance, called = create_tester(a_list, "clear", (), {})
        instance.clear()
        assert called[0]
        assert instance == []

    def test_list_extend(self, a_list):
        instance, called = create_tester(a_list, "extend", ([1, 2, 3],), {})
        instance.extend([1, 2, 3])
        assert called[0]
        assert instance == [1, 2, 3, 1, 2, 3]

    def test_list_insert(self, a_list):
        instance, called = create_tester(
            a_list,
            "insert",
            (
                0,
                1,
            ),
            {},
        )
        instance.insert(0, 1)
        assert called[0]
        assert instance == [1, 1, 2, 3]

    def test_list_pop(self, a_list):
        instance, called = create_tester(a_list, "pop", (0,), {})
        instance.pop(0)
        assert called[0]
        assert instance == [2, 3]

    def test_list_remove(self, a_list):
        instance, called = create_tester(a_list, "remove", (1,), {})
        instance.remove(1)
        assert called[0]
        assert instance == [2, 3]

    def test_list_sort(self, a_list):
        instance, called = create_tester(a_list, "sort", (), {})
        instance.sort()
        assert called[0]
        assert instance == [1, 2, 3]

    def test_list___setitem__(self, a_list):
        instance, called = create_tester(a_list, "setitem", (1, 4), {})
        instance[1] = 4
        assert called[0]
        assert instance == [1, 4, 3]
