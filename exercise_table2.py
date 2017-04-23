import unittest
import time
from selenium import webdriver

class ExerciseOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testExerciseOne(self):
        driver = self.driver
        driver.get("http://www.salzerdesign.com/test/fixedTable.html")

        # Elements
        list = []

        for i in range(0, 6):
            row = driver.find_element_by_xpath(
                "//table[@id='tablesorter-demo']/tbody/tr[" + str(i + 1) + "]/td[4]")
            list.append(row.text.encode('UTF8')[1:])

        y = sorted(list, key=float)
        print y
        print '-------------------'

        for i in range(0, 6):
            row = driver.find_element_by_xpath(
                "//table[@id='tablesorter-demo']/tbody/tr[" + str(i + 1) + "]")
            cell = driver.find_element_by_xpath(
                "//table[@id='tablesorter-demo']/tbody/tr[" + str(i + 1) + "]/td[4]")

            if cell.text == "$" + y[0]:
                print "Lowest price is:"
                print row.text
                print "-----------------"

            if cell.text == "$" + y[-1]:
                print "Highest price is:"
                print row.text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
