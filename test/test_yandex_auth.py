from selenium import webdriver
import time
import unittest


class test_auth_yandex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://passport.yandex.ru/auth')

    def test_auth(self):

        input_login = '//*[@id="passp-field-login"]'
        login = '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/form/div[3]/button'
        input_data = self.driver.find_element_by_xpath(input_login)
        input_data.send_keys('TestAuth')
        time.sleep(0.5)
        auth = self.driver.find_element_by_xpath(login)
        auth.click()
        time.sleep(2)

        #проверка что совершен переход на страницу ввода пороля(найдена графа "не помню пороль")
        path_pass = '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/form/div[2]/div/div[2]/a'
        password = self.driver.find_element_by_xpath(path_pass)
        self.assertIsNotNone(password)


