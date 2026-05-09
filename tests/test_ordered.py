import time

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_urAddrInfo import checkout_urAddrInfo
from pages.order_overview import OrderOverview

def test_ordered(setup):
    driver = setup
    lp = LoginPage(driver)
    pp = ProductPage(driver)
    ck = CartPage(driver)
    ad = checkout_urAddrInfo(driver)
    oo = OrderOverview(driver)

    lp.open_url()
    time.sleep(2)
    lp.login("standard_user", "secret_sauce")
    time.sleep(3)
    pp.add_to_cart()
    time.sleep(2)
    pp.go_to_cart()
    time.sleep(3)
    ck.checkout()
    time.sleep(3)
    ad.checkout_info("Jyoti","Matt","112233")
    time.sleep(2)
    oo.order_overview()
    time.sleep(4)