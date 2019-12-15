import  npsp.constants  as CONST
class Utilities(object):


    @classmethod
    def verify_one_item_list(cls, elem_list):
        """
        Checks that a single item was found for a given find_by selector; Used when a single element is expected
        The find_by methods return a list of elements matching the locator used.
        :param elem_list: The browser.find_by... methods return a list of WebDriverElements

        :return: elem_list[0] the single item is returned

        :raise: Exception if list has more than one item
        """
        if not len(elem_list) == 1:
            raise Exception("More that one item found")
        return elem_list[0]

    @classmethod
    def do_npsp_login(cls, browser):
        """
        Use as the standard method to begin Opportunity Application testing.
        Handles the authentication and navigation to Opportunities Home and performs verification of the page.
        """
        with browser:
            browser.visit(CONST.NPSPSALESFORCE)
        # TODO  refactor the Opportunity "def test_do_login(self):"
        # TODO  investigate handling two factor authentication

    @classmethod
    def verify_login_page(cls, browser, elems):
        """
        These elements must be found on the page
        :param browser: browser instance performing the work
        :param elems: element info dictionary as selector: validator()

        :return: True/False
        """
        # TODO implement
        return True
