import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from Pages.Homepage import Home, CartItems
from Pages.orderpage import Order
from utilites.argpass import excu, browser


class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        self.excu = excu
        self.browser = browser
        self.flag = False
        if excu == 'Local':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=s)
                self.driver.implicitly_wait(30)
                self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
                self.action = ActionChains(self.driver)
                self.wait = WebDriverWait(self.driver, 60)
            elif browser == 'firefox':
                self.driver = webdriver.Firefox(service=s)
                self.driver.implicitly_wait(30)
                self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
                self.action = ActionChains(self.driver)
                self.wait = WebDriverWait(self.driver, 60)
            elif browser == 'edge':
                self.driver = webdriver.Edge(service=s)
                self.driver.implicitly_wait(30)
                self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
                self.action = ActionChains(self.driver)
                self.wait = WebDriverWait(self.driver, 60)
            else:
                print("Please choose correct driver")
        if excu == 'Grid':
            if browser == "chrome":
                self.driver = webdriver.Remote(
                    command_executor='http://192.168.1.100:4444/wd/hub')

            elif browser == "firefox":
                # Local webdriver implementation
                # web_driver = webdriver.Firefox()
                # Remote WebDriver implementation
                self.driver = webdriver.Remote(
                    command_executor='http://192.168.1.100:4444/wd/hub')
            else:
                print("Please choose correct driver")


    def test_cart(self):
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
