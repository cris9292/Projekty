# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep

valid_fullname = "Krzysztof Malolepszy"
invalid_email = "12!3opwgmail.com"
valid_password = "Password123@!"

class AliexpressRegisteration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/?lang=pl")

    def test_invalid_email(self):
        driver = self.driver
        zaloguj = driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[1]')
        zaloguj.click()
        driver.implicitly_wait(3)
        imie = driver.find_element_by_id('full-name')
        imie.send_keys(valid_fullname)
        haslo = driver.find_element_by_id('password')
        haslo.send_keys(valid_password)
        email = driver.find_element_by_id('email')
        email.send_keys(invalid_email)
        sleep(3)
        error_notice = driver.find_element_by_xpath('//*[@id="phx-signup-form"]/div[1]/div[2]/div/div[1]/p[3]')
        print(error_notice.text)
        assert error_notice.is_displayed
        self.assertEqual(error_notice.text, u"Wprowadź prawidłowy adres e-mail.")



    def tearDown(self):
       self.driver.quit()

if __name__ == "__main__":
    unittest.main()
