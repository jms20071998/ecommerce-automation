import pytest
from utils.read_data import get_data
from pages.login_page import LoginPage

@pytest.mark.parametrize("data", get_data())
def test_login_multiple(setup, data):
    driver = setup
    lp = LoginPage(driver)

    lp.open_url()
    lp.login(data["username"], data["password"])