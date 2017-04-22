import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExerciseOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testExerciseOne(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        # Elements
        link = driver.find_element_by_xpath("//a[contains(@class, 'kaloyan')]")

        link.click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")

        firstname = driver.find_element_by_xpath("//input[1]")
        sex_male = driver.find_element_by_xpath("//input[@id='male']")
        lastname = driver.find_element_by_xpath("//input[@class='class-one']")
        checkbox_car = driver.find_element_by_xpath("//input[contains(@name, 'le2')]")
        submit = driver.find_element_by_xpath("//input[@id='submit']")

        firstname.send_keys("kaloyan")
        lastname.send_keys("ginchev")
        sex_male.click()
        checkbox_car.click()
        submit.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()