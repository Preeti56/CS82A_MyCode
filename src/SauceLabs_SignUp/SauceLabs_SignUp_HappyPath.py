# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import helpers

form_fields = {
	"first_name" : "SauceLabs",
	"last_name" : "Automation",
	"email" : helpers.generate_email(date_stamp=helpers.generate_date_stamp()),
	"company" : "Foothill CS82A",
	"username" : helpers.generate_date_stamp(),
	"password" : "",
	"password_confirm" : ""
	}
	
class SauceLabsSignUpHappyPath(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/signup/trial"
        self.verificationErrors = []
            
    def test_sauce_labs_sign_up_happy_path(self):
    	driver = self.driver
    	driver.get(self.base_url)
    	
    	for field in form_fields:
    		driver.find_element_by_id(field).send_keys(form_fields[field])
    	        
        #company size select from drop down
        Select(driver.find_element_by_id("company-size")).select_by_visible_text("Just Me")
        
        driver.find_element_by_id("submit-button").click()
        try: self.assertEqual('Sauce Labs | Account', driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
