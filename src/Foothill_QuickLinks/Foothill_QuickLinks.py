# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

dropdown_items = {
    "Behavioral Intervention" : "Behavior Evaluation | best",
    "BioHealth Division" : "Biological & Health",
    "Bookstore" : "Home",
    "Business & Social Sciences" : "Business and Social Sciences | bss"
    }

class FoothillQuickLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.foothill.edu/index.php"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_foothill_quick_links(self):
        driver = self.driver
       
        for dropdown_option in dropdown_items:
            driver.get(self.base_url)
            quick_list = driver.find_element_by_xpath("//select[@name='topnav']")
            Select(quick_list).select_by_visible_text(dropdown_option)
            expected_title = dropdown_items[dropdown_option]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))  
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
