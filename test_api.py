import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    response = requests.get(f"{BASE_URL}/add/{a}/{b}")
    assert response.status_code == 200
    assert response.json()["result"] == expected