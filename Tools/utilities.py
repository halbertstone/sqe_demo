import npsp.constants  as CONST
from npsp.opportunity_exceptions import Opportunity_Exception, Opportunity_Exception_Not_Implemented


class Utilities(object):
    @classmethod
    def navigate_to_new_opp_button(cls, browser):
        """
        Navigate from the NPSP Getting Started (login landing page) and return the WebDriverElement "New" Button
        corresponding to triggering the display of the New Opportunities Type Selector Dialog

        :param browser: splinter browser instance to perform the work

        :return: new_opp_button a WebDriverElement
            # TODO: Investigate methodology: return the new button and let the caller do the click, OR click it here and return the resulting dialog element??
        """
        # Expect to be on the Home Page: Getting Started Tab
        if not browser.is_text_present("Getting Started", 60):
            raise Opportunity_Exception("Getting Started not found")
        waffle_button = Utilities.get_element_by_css(browser, CONST.OPP_WAFFLE_SELECTOR)
        waffle_button.click()

        # Expect Overlay dialog to display
        # Enter search text "opportunities"
        search_input = Utilities.get_element_by_css(browser, CONST.OPP_SEARCH_INPUT_SELECTOR)
        search_input.fill("opportunities")
        opportunities_link = Utilities.get_element_by_css(browser, CONST.OPP_SEARCH_RESULT_SELECTOR)
        opportunities_link.click()

        # Do something here to verify the Opportunities Tab / Recently Viewed page is now displayed, like click it
        opp_tab_link = Utilities.get_element_by_css(browser, CONST.OPP_TAB_LINK_SELECTOR)
        opp_tab_link.click()

        # Now select the NEW button
        new_opp_button = Utilities.get_element_by_css(browser, CONST.OPP_NEW_BUTTON_SELECTOR)
        return new_opp_button

    @classmethod
    def get_element_by_css(cls, browser, css_selector):
        elem_list = browser.find_by_css(css_selector)
        return Utilities.verify_one_item_list(elem_list)

    @classmethod
    def verify_one_item_list(cls, elem_list):
        """
        Checks that a single item was found for a given find_by selector; Used when a single element is expected
        The find_by methods return a list of elements matching the locator used.
        :param elem_list: The browser.find_by... methods return a list of WebDriverElements

        :return: WebDriverElement from list: elem_list[0] the single item is returned

        :raise: Exception if list has more than one item
        """
        if not len(elem_list) == 1:
            raise Exception("More that one item found")
        return elem_list[0]

    @classmethod
    def navigate_open_new_opportunity_form(cls, browser, opt_type):
        """
        Cause the new opportunity form to display for a selected opportunity type.

        :param browser: splinter browser instance to do the work
        :param opt_type: Opportunity type select class that maps to a new opportunity choice selection
        :return: The form selector to be used as a local root for a page/region of interest
            # TODO: Investigate methodology: return the new button and let the caller do the click, OR click it here and return the resulting dialog element??
        """
        raise Opportunity_Exception_Not_Implemented("Not Implemented")

    @classmethod
    def do_npsp_login(cls, browser):
        """
        Use as the standard method to begin Opportunity Application testing.
        Handles the authentication and navigation to Opportunities Home and performs verification of the page.
        """
        # TODO  refactor the Opportunity "def test_do_login(self):"
        # TODO  investigate handling two factor authentication
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

            # TODO: Handle pop-up about Notifications Block/Allow that can occur at this point
            # NOTE: Must Verify that the npsp home page has displayed (more than above wait for it)
            home_page_welcome_list = browser.find_by_css(CONST.HOME_PAGE_WELCOME_SELECTOR)
            home_page_welcome_text = Utilities.verify_one_item_list(home_page_welcome_list)
            if CONST.HOME_EXPECTED_WELCOME_TEXT in home_page_welcome_text.value:
                raise Opportunity_Exception("Not expected welcome text")
            # TODO: include more page validation: self.assert something else to verify the correct page is displaying

    @classmethod
    def verify_login_page(cls, browser, elems):
        """
        These elements must be found on the page
        :param browser: browser instance performing the work
        :param elems: element info dictionary as selector: validator()

        :return: True/False
        """
        # TODO implement
        print(f"These items found: {elems.items()}")
        return True

    @classmethod
    def verify_elements(cls, browser, elems):
        """
        These elements must be found on the page
        :param browser: browser instance performing the work
        :param elems: element info dictionary as selector: validator()

        :return: True/False
        """
        # TODO implement
        for k, v in elems.items():
            v(k)
        return True

    @classmethod
    def do_verify_elements(cls, browser, elems):
        """
        These elements must be found on the page
        :param browser: browser instance performing the work
        :param elems: element info dictionary as selector: validator()

        :return: True/False
        """
        # TODO implement
        for v in elems.items():
            exec(v)
        return True

    @classmethod
    def opp_type_picker(cls, browser, drop_down_selector):
        """
        Given a type to select, makes the selection and clicks the next button
        :param drop_down_selector: The selector for the new opportunity form type to display
        :return: selector (css) for the new form
        """
        # Expect an overlay dialog with text "SELECT A RECORD TYPE"
        text_select_record_type = Utilities.get_element_by_css(browser, CONST.OPP_SELECT_TYPE_LEGEND_SELECTOR)
        if not text_select_record_type.value() == CONST.OPP_TEXT_SELECT_TYPE:
            raise Opportunity_Exception(
                "Did not find expected overlay dialog for selection of the new Opportunity type")
        # TODO: Verify that all expected radio button choices are available
        # TODO: Verify that radio button selection behavior, specifically only one choice at a time
        # TODO: Investigate what is the change that is equivalent to a real Radio Button attribbute checked=True
        opp_grant_radio = Utilities.get_element_by_css(browser, CONST.OPP_TYPE_GRANT_SELECTOR)
        opp_grant_radio.click()  # This a class="slds-radio--faux" so not sure how to verify the click actually selected it
        # Assuming it was selected
        # TODO: TEST Branch:  Select the cancel button and verify correct cancel behavior
        # Click on the NEXT button
        opp_type_next_button = Utilities.get_element_by_css(browser, CONST.OPP_TYPE_NEXT_BUTTON__SELECTOR)
        opp_type_next_button.click()

        # EXPECT Overlay dialog "New Opportunity: Grant"
