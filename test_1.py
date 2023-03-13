import pytest

@pytest.mark.usefixtures("mod_func")
class modTests:
    def test_one(self):
        print("in module1")

class mod1Tests:
    def test_two(self):
        print("in module11")

