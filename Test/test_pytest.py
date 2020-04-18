from collections import namedtuple
import pytest

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42



Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Без использования параметров, следует ссылаться на значения по умолчанию."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Проверка свойства .field (поля) namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

# def test_one():
#     assert (1, 2, 3) == (1, 2, 3)

# def test_two():
#     assert None is "all"
#
# def test_three():
#     assert True