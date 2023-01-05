import pytest


def test_pass():
    pass


def test_fail():
    assert False


@pytest.mark.skip
def test_skip():
    pass
