import time

from selenium.webdriver.common.by import By

from Locators.locators import PageLocator as pl
class Home:
    def __init__(self,driver):
        self.driver=driver
        self.srchbtn=pl.srchbtn
        self.products=pl.products
        self.prodtit=pl.prodtit
        self.addtocart=pl.addtocart
    def searchitem(self,item):
        driver=self.driver
        driver.find_element(By.XPATH, self.srchbtn).send_keys(item)
    def searchproduct(self):
        driver=self.driver
        products = driver.find_elements(By.XPATH, self.products)
        for product in products:
            title = product.find_element(By.XPATH, self.prodtit)
            print(title.text)
            product.find_element(By.XPATH, self.addtocart).click()
            time.sleep(1)
class CartItems:
    def __init__(self,driver):
        self.driver=driver
        self.checkitm=pl.checkitm
        self.procbtn=pl.procbtn
    def chec_and_processed(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.checkitm).click()
        driver.find_element(By.XPATH, self.procbtn).click()




