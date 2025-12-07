import pytest

@pytest.fixture
def test_qq():
    return {"username": "test_user", "email": "test@example.com"}

def test_qq1(test_qq):
    assert test_qq["username"] == "tes1t_user"
