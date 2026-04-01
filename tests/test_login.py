from pages.login_page import LoginPage

def test_valid_login(setup):
   driver = setup
   lp = LoginPage(driver)

   lp.open_url()
   lp.login("standard_user", "secret_sauce")
   assert "inventory" in driver.current_url
