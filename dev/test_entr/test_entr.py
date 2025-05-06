# from .web import valid_url
from dev.test_entr.web import valid_url

def test_starts_correctly():
    assert valid_url("http://yoyo.com")
    assert valid_url("https://yoyo.com")
    assert not valid_url("foobar.co")
