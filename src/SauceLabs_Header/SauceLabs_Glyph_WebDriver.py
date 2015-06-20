# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest

header_dropdown_links = {
        "Features" : "Features",
        "Company" : "Company | Values",
        "Community" : "Community | Open Sauce",
        "Solutions" : "Selenium Testing | Solutions",
        "Resources" : "Resources",
        "Enterprise" : "Enterprise",
        "Sign Up" : "Sign Up",
        "Docs" : "Docs",
        "Pricing" : "Pricing",
        "Login" : "Login"      
    }

class SauceLabsHeader(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sauce_labs_header(self):
        driver = self.driver
        
       # for link in header_dropdown_links:
        driver.get(self.base_url)
        menuIcon = driver.find_element_by_class_name("hamburger")
        menuIcon.click()
        #driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
        menuIcon.find_element_by_link_text("Pricing").click()
        try: self.assertRegexpMatches(driver.title,"Pricing")
            #driver.find_element_by_link_text(link).click()
            #expected_title = header_dropdown_links[link]
        #try: self.assertRegexpMatches(driver.title,expected_title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
