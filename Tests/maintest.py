import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.Homepage import Home, CartItems
from Pages.orderpage import Order


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.implicitly_wait(10)

    def testcart(self):
        driver = self.driver
        home = Home(driver)
        home.searchitem("ca")
        time.sleep(2)
        home.searchproduct()

        cartIcon = CartItems(driver)
        cartIcon.chec_and_processed()

        order = Order(driver)
        order.aplly_promocode("rahulshettyacademy")
        order.purchase_Item()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
