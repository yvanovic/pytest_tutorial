class Dog:
    """Dog Class"""
    pass

def test_objects_are_objects():
    fido = Dog()
    assert True == isinstance(fido, object)
    assert True == isinstance(fido, Dog)