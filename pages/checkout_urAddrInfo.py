import time

from selenium.webdriver.common.by import By

class checkout_urAddrInfo:
    def __init__(self, driver):
        self.driver = driver
    def checkout_info(self, Fname, Lname, PostalCode):
        self.driver.find_element(By.ID, "first-name").send_keys(Fname)
        time.sleep(4)
        self.driver.find_element(By.ID, "last-name").send_keys(Lname)
        time.sleep(2)
        self.driver.find_element(By.ID,"postal-code").send_keys(PostalCode)
        time.sleep(2)
        self.driver.find_element(By.ID,"continue").click()
        print("Address is added")
        time.sleep(3)