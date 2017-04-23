import unittest
import time
from selenium import webdriver


class ExerciseOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testExerciseOne(self):
        driver = self.driver
        driver.get("http://toolsqa.com/automation-practice-table/")

        # Elements
        dubai_td = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]")
        print dubai_td.text

        row = driver.find_element_by_xpath("//table/tbody/tr[2]/td")
        print row.text
        print '---------------------'

        for i in range(0, 4):
            print driver.find_element_by_xpath("//table/tbody/tr[" + str(i + 1) + "]/td[1]").text

            if i == 1:
                print driver.find_element_by_xpath("//table/tbody/tr[" + str(i + 1) + "]/td[2]").text

            if i == 2:
                print driver.find_element_by_xpath("//table/tbody/tr[" + str(i + 1) + "]/td[3]").text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
