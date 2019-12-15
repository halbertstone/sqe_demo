## ========================
## CONSTANTS
## ========================

# -----------------
# URL
# -----------------
SALESFORCEORG = "https://www.salesforce.org/"
NPSPSALESFORCE = "https://login.salesforce.com/"

# -----------------
# LOGIN PAGE
# -----------------
LOGIN_LOGO_IMG_SELECTOR = "#logo"
LOGIN_USERNAME_LABEL_SELECTOR = "#usernamegroup > label"
LOGIN_USERNAME_INPUT_SELECTOR = "#username"
LOGIN_USERNAME_INPUT_ID = "username"
LOGIN_PASSWORD_LABEL_SELECTOR = "#login_form > label"
LOGIN_PASSWORD_INPUT_SELECTOR = "#password"
LOGIN_PASSWORD_INPUT_ID = "password"
LOGIN_SUBMIT_LOGIN_SELECTOR = "#Login"
LOGIN_SUBMIT_LOGIN_ID = "Login"
LOGIN_WRONG_PASSWORD = "hstone@npsp.orgBADPWD"
LOGIN_ERROR_ID = "error"
LOGIN_EXPECTED_ERROR_TEXT = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
LOGIN_GOOD_PASSWORD = "***********"
LOGIN_TEST_USER = "hstone@npsp.org"

# -----------------
# SECOND_FACTOR PAGE
# -----------------
SECOND_FACTOR_SELECTOR = "#smc"
SECOND_FACTOR_ID = "smc"

# -----------------
# HOME PAGE
# -----------------

HOME_PAGE_WELCOME_SELECTOR = "#j_id0\:j_id2 > div > div:nth-child(2) > h1"
HOME_EXPECTED_WELCOME_TEXT = "Welcome to Salesforce and the Nonprofit Success Pack (NPSP)!"