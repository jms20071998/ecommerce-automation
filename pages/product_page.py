from threading import Thread

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        print("Clicked Add to Cart")
    # def go_to_cart(self):
    #     self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def go_to_cart(self):  # method to open cart page
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)

    def is_product_added(self):
        items = self.driver.find_elements("class name", "cart_item")
        items = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return items.text
            # getting list of items in cart
        # return len(items) > 0

