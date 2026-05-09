import time

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

def test_checout(setup):
    driver = setup
    ck = CartPage(driver)
    lp = LoginPage(driver)
    pp = ProductPage(driver)

    lp.open_url()
    lp.login("standard_user", "secret_sauce")
    pp.add_to_cart()
    pp.go_to_cart()
    time.sleep(3)
    ck.checkout()