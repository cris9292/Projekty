# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep

valid_name = "Krzysztof"
valid_surname = "Malolepszy"
invalid_email = "alamakotagmail.com"
valid_password = "Password123@!"

class EbouwieRegisteration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")

    def test_invalid_email(self):
        driver = self.driver
        zaloguj = driver.find_element_by_xpath('//*[@id="top"]/body/header/div[3]/div/div[2]/a[2]')
        zaloguj.click()
        imie = driver.find_element_by_id('firstname')
        imie.send_keys(valid_name)
        nazwisko = driver.find_element_by_id('lastname')
        nazwisko. send_keys(valid_surname)
        haslo = driver.find_element_by_id('password')
        haslo.send_keys(valid_password)
        haslo_potwierdzenie = driver.find_element_by_id('confirmation')
        haslo_potwierdzenie.send_keys(valid_password)
        email = driver.find_element_by_id('email_address')
        email.send_keys(invalid_email)
        policy = driver.find_element_by_xpath('//*[@id="form-validate"]/label[2]/input')
        policy.click()
        error_notice = driver.find_element_by_xpath('//*[@id="form-validate"]/div[3]/span')
        print(error_notice.text)
        assert error_notice.is_displayed
        self.assertEqual(error_notice.text, u"Wprowadzono niepoprawny adres e-mail")



    def tearDown(self):
       self.driver.quit()

if __name__ == "__main__":
    unittest.main()
