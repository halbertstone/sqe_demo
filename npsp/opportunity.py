import unittest

from selenium import webdriver
from splinter import Browser

import npsp.constants as CONST
from Tools.utilities import Utilities
from npsp.opportunity_exceptions import Opportunity_Exception


class MyTestCase(unittest.TestCase):

    def test_do_login(self):
        chrome_options = webdriver.ChromeOptions()
        browser = Browser('chrome', options=chrome_options)

        with browser:
            browser.visit(CONST.NPSPSALESFORCE)

            # Find the page elements needed
            username_input_list = browser.find_by_id(CONST.LOGIN_USERNAME_INPUT_ID)
            password_input_list = browser.find_by_id(CONST.LOGIN_PASSWORD_INPUT_ID)
            submit_login_list = browser.find_by_id(CONST.LOGIN_SUBMIT_LOGIN_ID)

            # Get the single item from the list returned by 'find_by'
            username_input = Utilities.verify_one_item_list(username_input_list)
            password_input = Utilities.verify_one_item_list(password_input_list)
            submit_input = Utilities.verify_one_item_list(submit_login_list)

            # Verify these elements are visible and enabled
            if not username_input.visible:
                raise Opportunity_Exception("username_input field found but not visible")
            if not password_input.visible:
                raise Opportunity_Exception("password_input field found but not visible")
            if not submit_input.visible:
                raise Opportunity_Exception("submit_input field found but not visible")

            # Ready to proceed, enter credentials and submit
            username_input.fill(CONST.LOGIN_TEST_USER)
            password_input.fill(CONST.LOGIN_GOOD_PASSWORD)
            submit_input.click()

            # NOTE: Should have a wait for the two factor authentication
            # NOTE: Problem Verifying can occur at this time preventing login therefore test fails with exception
            while browser.is_element_not_present_by_id(CONST.TWO_FACTOR_ID, 60):
                if browser.is_text_present(CONST.TWO_FACTOR_CANNOT_SEND):
                    raise Opportunity_Exception(
                        "Two factor authentication mechanism cannot send code at this time; System Failure")

            print("DEBUG: Found CONST.TWO_FACTOR_ID {0}".format(CONST.TWO_FACTOR_ID))

            # NOTE:  MANUAL operation to enter a code sent via SMS occurs at this point.
            # -- enter the code
            # -- click the verify action element/button
            # TODO: Investigate best practice at Salesforce for test execution with two factor

            # Need to wait for the Two Factor Auth process to complete and the Home page loads
            while browser.is_element_not_present_by_css(CONST.HOME_PAGE_WELCOME_SELECTOR, 60):
                pass

            print("DEBUG: Found CONST.TWO_FACTOR_ID {0}".format(CONST.TWO_FACTOR_ID))

            # TODO: Handle pop-up about Notifications Block/Allow that can occur at this point
            # NOTE: Must Verify that the npsp home page has displayed (more than above wait for it)
            home_page_welcome_list = browser.find_by_css(CONST.HOME_PAGE_WELCOME_SELECTOR)
            home_page_welcome_text = Utilities.verify_one_item_list(home_page_welcome_list)
            self.assertEqual(CONST.HOME_EXPECTED_WELCOME_TEXT, home_page_welcome_text.value,
                             "Not expected welcome text")
            # TODO: include more page validation: self.assert something else to verify the correct page is displaying

    def test_do_login_bad_password(self):
        chrome_options = webdriver.ChromeOptions()
        browser = Browser('chrome', options=chrome_options)

        with browser:
            browser.visit(CONST.NPSPSALESFORCE)

            # Find the page elements needed
            username_input_list = browser.find_by_id(CONST.LOGIN_USERNAME_INPUT_ID)
            password_input_list = browser.find_by_id(CONST.LOGIN_PASSWORD_INPUT_ID)
            submit_login_list = browser.find_by_id(CONST.LOGIN_SUBMIT_LOGIN_ID)

            # Get the single item from the list returned by 'find_by'
            username_input = Utilities.verify_one_item_list(username_input_list)
            password_input = Utilities.verify_one_item_list(password_input_list)
            submit_input = Utilities.verify_one_item_list(submit_login_list)

            # Verify these elements are visible and enabled
            if not username_input.visible:
                raise Opportunity_Exception("username_input field found but not visible")
            if not password_input.visible:
                raise Opportunity_Exception("password_input field found but not visible")
            if not submit_input.visible:
                raise Opportunity_Exception("submit_input field found but not visible")

            # Ready to proceed, enter credentials and submit
            username_input.fill(CONST.LOGIN_TEST_USER)

            password_input.fill(CONST.LOGIN_WRONG_PASSWORD)
            submit_input.click()

            ## Expect Error to be caught and message issued
            error_text_list = browser.find_by_id(CONST.LOGIN_ERROR_ID)
            error_text_elem = Utilities.verify_one_item_list(error_text_list)
            self.assertEqual(error_text_elem.text, CONST.LOGIN_EXPECTED_ERROR_TEXT, "Did not receive expected error")
