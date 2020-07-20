import unittest
# import HtmlTestRunner
import xmlrunner
from selenium import webdriver
import time
import sys

sys.path.append("C:/Users/User/Desktop/python/POM")
from Pages.login_page import LoginPage


class LoginTest(unittest.TestCase):
    base_url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()
    driver.maximize_window()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()

    def test_login(self):
        login = LoginPage(self.driver)
        login.set_username(self.username)
        login.set_password(self.password)
        login.click_login()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "web page title is not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\User\Desktop\python\POM\Reports'))
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/home/sheetal/PycharmProjects/PageObjectModel/Reports'))
