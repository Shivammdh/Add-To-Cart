import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Pages.Homepage import Home,CartItems
from Pages.orderpage import Order
port=["6666","8888","5555"]
for p in port:
    class MyTest(unittest.TestCase):
        def setUp(self) -> None:
            s=Service("D:/Selenium/chromedriver.exe")
            self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True,})
            self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
            self.driver.implicitly_wait(10)

        def testcart(self):
            driver=self.driver
            home=Home(driver)
            home.searchitem("ca")
            time.sleep(2)
            home.searchproduct()

            cartIcon=CartItems(driver)
            cartIcon.chec_and_processed()

            order=Order(driver)
            order.aplly_promocode("rahulshettyacademy")
            order.purchase_Item()
        def tearDown(self) -> None:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()