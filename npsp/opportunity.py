import unittest
from selenium import webdriver
from splinter import Browser
from Tools.utilities import Utilities
import npsp.constants as CONST

# import splinter.driver.webdriver.WebDriverElement
#
# ## ========================
# ## CONSTANTS
# ## ========================
#
#
# SALESFORCEORG = "https://www.salesforce.org/"
# NPSPSALESFORCE = "https://login.salesforce.com/"
#
# LOGIN_LOGO_IMG_SELECTOR = "#logo"
# LOGIN_USERNAME_LABEL_SELECTOR = "#usernamegroup > label"
# LOGIN_USERNAME_INPUT_SELECTOR = "#username"
# LOGIN_USERNAME_INPUT_ID = "username"
# LOGIN_PASSWORD_LABEL_SELECTOR = "#login_form > label"
# LOGIN_PASSWORD_INPUT_SELECTOR = "#password"
# LOGIN_PASSWORD_INPUT_ID = "password"
# LOGIN_SUBMIT_LOGIN_SELECTOR = "#Login"
# LOGIN_SUBMIT_LOGIN_ID = "Login"
# LOGIN_WRONG_PASSWORD = "hstone@npsp.orgBADPWD"
# LOGIN_ERROR_ID = "error"
# LOGIN_EXPECTED_ERROR_TEXT = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
# LOGIN_GOOD_PASSWORD = "npsP.org1!"
# LOGIN_TEST_USER = "hstone@npsp.org"
#
# SECOND_FACTOR_SELECTOR = "#smc"
# SECOND_FACTOR_ID = "smc"
#
# HOME_PAGE_WELCOME_SELECTOR = "#j_id0\:j_id2 > div > div:nth-child(2) > h1"
# HOME_EXPECTED_WELCOME_TEXT = "Welcome to Salesforce and the Nonprofit Success Pack (NPSP)!"

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
                raise Exception("username_input field found but not visible")
            if not password_input.visible:
                raise Exception("password_input field found but not visible")
            if not submit_input.visible:
                raise Exception("submit_input field found but not visible")

            # Ready to proceed, enter credentials and submit
            username_input.fill(CONST.LOGIN_TEST_USER)
            password_input.fill(CONST.LOGIN_GOOD_PASSWORD)
            submit_input.click()

            if browser.is_text_present("We can't send you a verification code right now. Please try again later", 2):
               raise Exception("Problem, service cannot perform two factor authentication")
            if not browser.is_text_present(CONST.HOME_EXPECTED_WELCOME_TEXT,30):
                raise Exception("Problem with login, did not find npsp home page welcome text")
            # NOTE: Problem Verifying can occur at this time
            # NOTE: Should have a wait for page to load at this point, AND the two factor authentication
            #       requires MANUAL input of a token from SMS so needs time
            # < p > We can't send you a verification code right now. Please try again later.</p>





            while browser.is_element_not_present_by_id(CONST.SECOND_FACTOR_ID, 60):
                pass
            # NOTE:  MANUAL operation to enter a code sent via SMS occurs at this point.
            # -- enter the code
            # -- click the verify action element/button
            # TODO: Investigate best practice at Saleforce for test execution with two factor
            # while browser.is_element_not_present_by_css(CONST.HOME_PAGE_WELCOME_SELECTOR, 5):
            #     pass
            # TODO: Handle pop-up about Notifications Block/Allow that can occur at this point
            # NOTE: Must Verify that the npsp home page has displayed (more than above wait for it)
            home_page_welcome_list = browser.find_by_css(CONST.HOME_PAGE_WELCOME_SELECTOR)
            home_page_welcome_text = Utilities.verify_login_page(home_page_welcome_list)
            self.assertEqual(CONST.HOME_EXPECTED_WELCOME_TEXT, home_page_welcome_text.value, "Not expected welcome text")
            # Some more page validation: self.assert something else to verify the correct page is displaying
            print("Done")


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
            raise Exception("username_input field found but not visible")
        if not password_input.visible:
            raise Exception("password_input field found but not visible")
        if not submit_input.visible:
            raise Exception("submit_input field found but not visible")

        # Ready to proceed, enter credentials and submit
        username_input.fill(CONST.LOGIN_TEST_USER)
        password_input.fill(CONST.LOGIN_WRONG_PASSWORD)
        submit_input.click()

        ## Expect Error to be caught and message issued
        error_text_list = browser.find_by_id(CONST.LOGIN_ERROR_ID)
        error_text_elem = Utilities.verify_one_item_list(error_text_list)
        self.assertEqual(error_text_elem.text, CONST.LOGIN_EXPECTED_ERROR_TEXT, "Did not receive expected error")

        print("Done")


if __name__ == '__main__':
    unittest.main()
