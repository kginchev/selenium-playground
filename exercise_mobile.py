import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ExerciseOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testExerciseOne(self):
        driver = self.driver
        driver.get("http://www.mobile.de")

        # Elements
        link = driver.find_element_by_xpath("//ul[@class='header-meta-actions']/li[3]")
        link.click()

        change_lang= driver.find_element_by_xpath("//a[contains(@href,'lang=en')]")
        change_lang.click()

        login= driver.find_element_by_xpath("//a[@id='hdmylogin']")
        login.click()

        username= driver.find_element_by_xpath("//input[@id='login-username']")
        username.send_keys("alibaba@gmail.com")

        password= driver.find_element_by_xpath("//input[@id='login-password']")
        password.send_keys("xxxxx" + Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
