import pytest

@pytest.mark.usefixtures("chrome_browser")
@pytest.mark.skip
class basicTests:

        def test_working_as_expected(self, chrome_browser):
                chrome_browser.get("https://google.com")
                print("test case 1")
                assert True

        def test_working_as_expected(self, chrome_browser):
                chrome_browser.get("https://firefox.com")
                print("test case 1")
                assert True

@pytest.mark.usefixtures("play_with_nos")
class numTests:

    def test_nums(self):
        assert self.text == 'a'
        print("hello1")

    def test_append(self):
        assert chan(self.text) == 'b'
        print("hello2")


def chan(str):
    str = 'b'
    return str

class BasicTests:
    def test_for_specific_browser(self,browser):
        browser.get("https://google.com")