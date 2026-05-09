import time

from selenium.webdriver.common.by import By

class OrderOverview:
    def __init__(self, driver):
        self.driver = driver
    def order_overview(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        print("Ordered")