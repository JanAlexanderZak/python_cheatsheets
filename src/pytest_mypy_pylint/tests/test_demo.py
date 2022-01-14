from src import demo
import pytest


def test_basics():
    pass


class TestAdd:

    # Describe in string and pass list of tuples.
    @pytest.mark.parametrize(
        'a, b, expected', [
            (1, 1, 2),
            (2, 3, 5),
        ]
    )
    def test_with_param(self, a, b, expected):
        assert demo.add(a, b) == expected

    def test_add(self):
        assert demo.add(1, 2) == 3

    def test_add_more(self):
        assert demo.add(1, 100) == 101

    def test_error(self):
        # Catch the error. Test expects the MysteryError.
        with pytest.raises(demo.MysteryError):
            demo.add(99, 1)


class TestSubtract:
    pass


# FIXTURES
# Each fixture has to be uniquely named.
def test_fixture(my_fixture):
    assert my_fixture == 42


def test_capsys(capsys):
    print('hello')
    print('bye')
    # Intercepts the print function.
    # That way it gets stored and can be accessed.
    out, err = capsys.readouterr()
    assert 'hello\n' in out


def test_capsys_more(capsys):
    print('hello')
    # Intercepts the print function.
    # That way it gets stored and can be accessed.
    out, err = capsys.readouterr()
    assert 'hello\n' == out


def test_monkeypatch(monkeypatch):
    def fake_add(a, b):
        return 42

    # File and name of fnc!
    monkeypatch.setattr(demo, "add", fake_add)
    assert demo.add(2, 3) == 42


def test_tempdir(tmpdir):
    # Create file handle.
    some_file = tmpdir.join('something.txt')
    some_file.write('{"hello": "world"}')

    # Does the read-in work?
    result = demo.read_json(str(some_file))
    assert result["hello"] == "world"


def test_fixture_with_fixtures(capsys, captured_print):
    print('more')
    out, err = capsys.readouterr()
    assert out == "hello\nmore\n"
