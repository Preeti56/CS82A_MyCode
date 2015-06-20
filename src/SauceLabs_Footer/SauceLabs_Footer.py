# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class SauceLabsFooter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
    
    def test_sauce_labs_footer(self):
        driver = self.driver
        
        driver.get(self.base_url)
        #from selenium IDE
        #driver.find_element_by_css_selector("a[title=\"Pricing\"]").click()
        driver.find_element_by_link_text("PRICING").click()
        try: self.assertRegexpMatches(driver.title, r"Pricing")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        #from selenium IDE
        #driver.find_element_by_css_selector("a[title=\"Enterprise\"]").click()
        driver.find_element_by_link_text("ENTERPRISE").click()
        try: self.assertRegexpMatches(driver.title, r"Enterprise")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        #from selenium IDE
        #driver.find_element_by_css_selector("a[title=\"Docs\"]").click()
        driver.find_element_by_link_text("DOCS").click()
        try: self.assertRegexpMatches(driver.title, r"Docs")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        #from selenium IDE
        #driver.find_element_by_css_selector("a[title=\"Platforms\"]").click()
        driver.find_element_by_link_text("PLATFORMS").click()
        try: self.assertRegexpMatches(driver.title, r"Platforms")
        except AssertionError as e: self.verificationErrors.append(str(e))
       
    def tearDown(self): 
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
