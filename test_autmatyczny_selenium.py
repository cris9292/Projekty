# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep

valid_name = "Krzysztof"
valid_surname = "Malolepszy"
valid_phonenumber = "654789321"
invalid_email = "12!3opwgmail.com"
valid_password = "Password123"

class WizzairRegisteration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")



    def test_invalid_email(self):
        driver = self.driver
        zaloguj_btn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_css_selector("#login-modal > form > div > p > button")
        rejestracja_btn.click()
        imie = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        imie.send_keys(valid_name)
        nazwisko = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko.send_keys(valid_surname)
        plec = driver.find_element_by_id('register-gender-male')
        plec.click()
        numer_telefon = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        numer_telefon.send_keys(valid_phonenumber)
        email = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input')
        email.send_keys(invalid_email)
        haslo = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        haslo.send_keys(valid_password)
        obywatelstwo = driver.find_element_by_xpath('//input[@placeholder="Obywatelstwo"]')
        obywatelstwo.click()
        country_to_choose = driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/label[164]')
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()
        policy = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[10]/span/label[1]')
        policy.click()
        error_notice = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span')
        print(error_notice.text)
        assert error_notice.is_displayed
        self.assertEqual(error_notice.text, u"Nieprawidłowy adres e-mail")
