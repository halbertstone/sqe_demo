from selenium import webdriver
from splinter import Browser
import  npsp.constants  as CONST
class Utilities(object):

    @classmethod
    def verify_login_page(cls, browser, elems):
        """
        These elements must be found on the page
        :param brower: browser instance performing the work
        :param elems: element info dictionary as selector: validator()

        :return: True/False
        """
        # TODO implement
        return True

    @classmethod
    def verify_one_item_list(cls, elem_list):
        """
        Checks that a single item was found in the list
        :param elem_list: The browser.findby... methods return a list of WebDriverElements

        :return: elem_list[0] the single item is returned

        :raise: Exception if list has more than one item
        """
        if not len(elem_list) == 1:
            raise Exception("More that one item found")
        return elem_list[0]

    @classmethod
    def do_npsp_login(cls, browser):
        with browser:
            browser.visit(NPSPSALESFORCE)

            # Find the page elements needed
            username_input_list = browser.find_by_id(CONLOGIN_USERNAME_INPUT_ID)
            password_input_list = browser.find_by_id(LOGIN_PASSWORD_INPUT_ID)
            submit_login_list = browser.find_by_id(LOGIN_SUBMIT_LOGIN_ID)

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
            username_input.fill(LOGIN_TEST_USER)
            password_input.fill(LOGIN_GOOD_PASSWORD)
            submit_input.click()

            # NOTE: Should have a wait for page to load at this point, AND the two factor authentication
            #       requires MANUAL input of a token from SMS so needs time

            while browser.is_element_not_present_by_id(SECOND_FACTOR_ID, 60):
                pass
            # NOTE:  MANUAL operation to enter a code sent via SMS occurs at this point.
            # -- enter the code
            # -- click the verify action element/button
            # TODO: Investigate best practice at Saleforce for test execution with two factor
            while browser.is_element_not_present_by_css(HOME_PAGE_WELCOME_SELECTOR, 60):
                pass

            # NOTE: Must Verify that the npsp home page has displayed (more than above wait for it)
            home_page_welcome_list = browser.find_by_css(HOME_PAGE_WELCOME_SELECTOR)
            home_page_welcome_text = Utilities.verify_login_page(home_page_welcome_list)
            self.assertEqual(HOME_EXPECTED_WELCOME_TEXT, home_page_welcome_text.value, "Not expected welcome text")
            # Some more page validation: self.assert something else to verify the correct page is displaying
            print("Done")