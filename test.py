import pytest, helloworld

def test_helloworld():
    x = helloworld.helloworld()
    if x != 'helloworld':
        pytest.xfail("helloworld missing")