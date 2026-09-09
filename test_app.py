from app import add_numbers


def test_add_numbers():
    result = add_numbers(5, 3)
    assert result == 8