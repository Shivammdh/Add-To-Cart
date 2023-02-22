from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import PageLocator as pl

class Order:
    def __init__(self,driver):
        self.driver=driver
        self.promocode=pl.promocode
        self.promobtn=pl.promobtn
        self.promoinfo=pl.promoinfo
        self.placeorder=pl.placeorder
        self.selctcountry=pl.selctcountry
        self.chbx=pl.chbx
        self.finalproc=pl.finalproc

    def aplly_promocode(self,prmcode):
        driver=self.driver
        driver.find_element(By.CSS_SELECTOR, self.promocode).send_keys(prmcode)
        driver.find_element(By.CSS_SELECTOR, self.promobtn).click()
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.promoinfo)))
        print(btn.text)
        driver.find_element(By.XPATH, self.placeorder).click()
    def purchase_Item(self):
        driver=self.driver
        select = Select(driver.find_element(By.XPATH, self.selctcountry))
        select.select_by_visible_text("India")
        driver.find_element(By.CSS_SELECTOR, self.chbx).click()
        driver.find_element(By.XPATH, self.finalproc).click()


