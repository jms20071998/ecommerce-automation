import time

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.checkout_urAddrInfo import checkout_urAddrInfo

def test_urAddrInfo(setup):
    driver = setup
    lp = LoginPage(driver)
    pp = ProductPage(driver)
    ck = CartPage(driver)
    ad = checkout_urAddrInfo(driver)

    lp.open_url()
    lp.login("standard_user", "secret_sauce")
    pp.add_to_cart()
    pp.go_to_cart()
    time.sleep(2)
    ck.checkout()
    time.sleep(2)
    ad.checkout_info()
    time.sleep(4)
