from pages.product_page import ProductPage
from pages.login_page import LoginPage

def test_add_to_cart(setup):
    driver = setup

    lp = LoginPage(driver)
    pp = ProductPage(driver)

    lp.open_url()
    lp.login("standard_user", "secret_sauce")
    pp.add_to_cart()
    pp.go_to_cart()

    assert pp.is_product_added()