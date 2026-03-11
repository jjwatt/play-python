from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

def test_asdict():
    """_asdict() should return a dict."""
    t_task = Task('do something', 'jesse', True, 21)
    t_dict = t_task._asdict()
    expected = {
        "summary": "do something",
        "owner": "jesse",
        "done": True,
        "id": 21
    }
    assert t_dict == expected

