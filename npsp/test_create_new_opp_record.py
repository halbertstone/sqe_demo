import unittest

from selenium import webdriver
from splinter import Browser

import npsp.constants as CONST
from Tools.utilities import Utilities
from npsp.opportunity_exceptions import Opportunity_Exception


class TestNewOpportunity(unittest.TestCase):

    def test_fill_new_opportunity_form_happy(self):
        """
        Use-Case:
        Full work-flow login, navigate to opportunity, create new grant record, edit record setting stage to Awarded

        Psudo-Code: RAW, not tested as Two Factor would not send verification code
        Strings have not been separated to the constants file


        Verify the happy path of submitting the minimum needed to create a new opportunity
        Just the required fields
        Stubs for handling creation of associated data require (methods for handing the likes of new contact, account,
        or handling selection of options from drop down list )

        #TODO statements inserted to record ideas
        """
        chrome_options = webdriver.ChromeOptions()
        browser = Browser('chrome', options=chrome_options)
        Utilities.do_npsp_login(browser)

        # Now select the NEW button
        new_opp_button = Utilities.navigate_to_new_opp_button(browser)
        new_opp_button.click()

        # Expect an overlay dialog with text "SELECT A RECORD TYPE"
        text_select_record_type = Utilities.get_element_by_css(browser, CONST.OPP_SELECT_TYPE_LEGEND_SELECTOR)
        if not text_select_record_type.value() == CONST.OPP_TEXT_SELECT_TYPE:
            raise Opportunity_Exception(
                "Did not find expected overlay dialog for selection of the new Opportunity type")
        # TODO: Verify that all expected radio button choices are available
        # TODO: Verify that radio button selection behavior, specifically only one choice at a time
        # TODO: Investigate what is the change that is equivalent to a real Radio Button attribbute checked=True

        # Select GRANT type opportunity
        opp_grant_radio = Utilities.get_element_by_css(browser, CONST.OPP_TYPE_GRANT_SELECTOR)
        opp_grant_radio.click()  # This a class="slds-radio--faux" so not sure how to verify the click actually selected it
        # Assuming it was selected
        # TODO: TEST Branch:  Select the cancel button and verify correct cancel behavior
        # Click on the NEXT button
        opp_type_next_button = Utilities.get_element_by_css(browser, CONST.OPP_TYPE_NEXT_BUTTON__SELECTOR)
        opp_type_next_button.click()

        # EXPECT Overlay dialog "New Opportunity: Grant"
        # Verify the "Opportunity Record Type" contains  "Grant"
        # TODO Investigate how to do this verification
        output_record_type = Utilities.get_element_by_css(browser,
                                                          "SOME SELECTOR for the field of the Output record type ")
        self.assertIn("Grant", output_record_type.value())

        # Fill in the required field values
        # TODO: Future: Verify that required fields have corresponding working error messages, style, content of msg
        # TODO: Investigate: What are the common fields for all the new opportunity forms
        # TODO: Future: Test input fields with bogus input to see if it is handled nicely or blows up
        # --- Required Fields on Grant
        # Opportunity Name
        # Account Name (Look up requires previously created object to select)
        #              New Account can be created from the drop-down list options: selector is "#\31 0175\:0 > span"
        #
        # Closing Date
        # Stage
        # TODO: Future: Test that all info text content are correct, expected on fields, content of message

        ### TODO ? BUG? Check if this is acceptable or a BUG: FORM allows negative dollar value
        ### TODO ? BUG? Check if it is acceptable to allow a PAST date entry

        # opp_name_field.fill("Silly Clowns")
        # opp_account_field
        # select
        # down
        # list
        # option
        # "Bigears"

        date_field = Utilities.get_element_by_css(browser,
                                                  CONST.OPP_FIELD_DATE_SELECTOR)
        date_field.fill("12/30/2019")
        stage_field = Utilities.get_element_by_css(browser, CONST.OPP_FIELD_STAGE_SELECTOR)
        # TODO: stage_field.select from the drop down list option "prospecting"

        # TODO: fill in optional fields with happy data
        # TODO: fill in optional fields with Bogus data to see what happens, hope they are handled nicely
        # TODO: TEST BRANCH: Select the Form Cancel button to verify expected behavior occurs
        # Select the Form Save button
        save_button = Utilities.get_element_by_css(browser, CONST.OPP_FORM_SAVE_BUTTON_SELECTOR)
        save_button.click()

        # Expect the new opportunity object is displayed.
        # Collect the current browser URL to extract the object ID value for future use
        test_opp_item_url = browser.url  # https://na174.lightning.force.com/lightning/r/Opportunity/0066g000002B0OMAA0/view
        parse_url = test_opp_item_url.split("/")  ## TODO: pull out of list the ID value

        # Now Edit the opportunity to set it as completed WON
        edit_button = Utilities.get_element_by_css(browser, CONST.OPP_RECORD_EDIT_BUTTON_SELECTOR)
        edit_button.click()

        ## Expect overlay dialog presenting form edit mode
        ## locate the 'stage' field
        stage_field = Utilities.get_element_by_css(browser, CONST.OPP_FIELD_STAGE_SELECTOR)
        # TODO: stage_field.select from the drop down option "Awarded"
        stage_field.selectdrop("Awarded")
        save_button = Utilities.get_element_by_css(browser, CONST.OPP_FORM_SAVE_BUTTON_SELECTOR)
        save_button.click()

        # Return to Opportunities List
        opp_list_view = Utilities.get_element_by_css(browser, CONST.OPP_TAB_LINK_SELECTOR)
