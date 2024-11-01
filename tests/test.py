from mypackage import mymodule
def test_add():
    """
    to makesure add works perfectly
    """
    assert mymodule.add(5,2) == 7, 'incorrect'
    assert mymodule.add(5,8) == 15, 'incorrect'