## ========================
## CONSTANTS
## ========================

# -----------------
# URL
# -----------------
NPSPSALESFORCE = "https://login.salesforce.com/"

# -----------------
# LOGIN PAGE
# -----------------
LOGIN_LOGO_IMG_SELECTOR = r"#logo"
LOGIN_USERNAME_LABEL_SELECTOR = r"#usernamegroup > label"
LOGIN_USERNAME_INPUT_SELECTOR = r"#username"
LOGIN_USERNAME_INPUT_ID = "username"
LOGIN_PASSWORD_LABEL_SELECTOR = r"#login_form > label"
LOGIN_PASSWORD_INPUT_SELECTOR = r"#password"
LOGIN_PASSWORD_INPUT_ID = "password"
LOGIN_SUBMIT_LOGIN_SELECTOR = r"#Login"
LOGIN_SUBMIT_LOGIN_ID = "Login"
LOGIN_WRONG_PASSWORD = "hstone@npsp.orgBADPWD"
LOGIN_ERROR_ID = "error"
LOGIN_EXPECTED_ERROR_TEXT = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
LOGIN_GOOD_PASSWORD = "***********"
LOGIN_TEST_USER = "hstone@npsp.org"

# -----------------
# SECOND_FACTOR PAGE
# -----------------
TWO_FACTOR_SELECTOR = "#smc"
TWO_FACTOR_ID = "smc"
TWO_FACTOR_CANNOT_SEND = "We can't send you a verification code right now. Please try again later."

# -----------------
# HOME PAGE
# -----------------

HOME_PAGE_WELCOME_SELECTOR = r"#j_id0\:j_id2 > div > div:nth-child(2) > h1"
HOME_EXPECTED_WELCOME_TEXT = "Welcome to Salesforce and the Nonprofit Success Pack (NPSP)!"
HOME_GETTING_STARTED_SELECTOR = r"#oneHeader > div.bBottom > one-appnav > div > one-app-nav-bar > nav > div > one-app-nav-bar-item-root.navItem.slds-context-bar__item.slds-shrink-none.slds-is-active > a"
# -----------------
# OPPORTUNITIES PAGE
# -----------------

OPP_WAFFLE_SELECTOR = r"#oneHeader > div.bBottom > one-appnav > div > div > div > nav"
OPP_SEARCH_INPUT_SELECTOR = r"#\31 8\:1330\;a"
OPP_SEARCH_RESULT_SELECTOR = r"#content_235\:1330\;a > div > div.slds-p-left--small > div > div.slds-section__content.list-ctr > ul > li:nth-child(48) > a"
OPP_TAB_LINK_SELECTOR = r"#oneHeader > div.bBottom > one-appnav > div > one-app-nav-bar > nav > div > one-app-nav-bar-item-root.navItem.slds-context-bar__item.slds-shrink-none.slds-is-active > a"
# seems to be same later r"#oneHeader > div.bBottom > one-appnav > div > one-app-nav-bar > nav > div > one-app-nav-bar-item-root.navItem.slds-context-bar__item.slds-shrink-none.slds-is-active > a"

OPP_RECENTLY_VIEWED_TEXT_SELECTOR = r"#brandBand_1 > div > div.center.oneCenterStage.lafSinglePaneWindowManager > div > div > div > div.slds-page-header--object-home.slds-page-header_joined.slds-page-header_bleed.slds-page-header.slds-shrink-none.test-headerRegion.forceListViewManagerHeader > div:nth-child(1) > div.slds-col.slds-has-flexi-truncate.firstHeaderRow > div > div.slds-media__body.slds-align-middle > div > h1 > div > div > span.triggerLinkText.selectedListView.uiOutputText"
OPP_NEW_BUTTON_SELECTOR = r"#brandBand_1 > div > div.center.oneCenterStage.lafSinglePaneWindowManager > div > div > div > div.slds-page-header--object-home.slds-page-header_joined.slds-page-header_bleed.slds-page-header.slds-shrink-none.test-headerRegion.forceListViewManagerHeader > div:nth-child(1) > div.slds-col.slds-no-flex.slds-grid.slds-align-top.slds-p-bottom--xx-small.test-lvmForceActionsContainer > ul > li > a"
OPP_SELECT_TYPE_LEGEND_SELECTOR = r"#content_1379\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeLeftColumn > legend"
OPP_TEXT_SELECT_TYPE = "Select a record type"
OPP_TYPE_GRANT_SELECTOR = r"#content_1379\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(3) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_DONATION_SELECTOR = r"#content_1379\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(1) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_IN_KIND_SELECTOR = r"#content_581\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(5) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_MAJOR_SELECTOR = r"#content_581\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(7) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_MATCH_SELECTOR = r"#content_581\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(9) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_MEMBER_SELECTOR = r"#content_581\:0 > div > div > div.actionBody > div > div > div:nth-child(1) > fieldset > div.changeRecordTypeRightColumn.slds-form-element__control > div:nth-child(11) > label > div.changeRecordTypeOptionRightColumn > span"
OPP_TYPE_CANCEL_BUTTON_SELECTOR = r"#content_581\:0 > div > div > div.inlineFooter > div > button.slds-button.slds-button--neutral.slds-button.slds-button_neutral.uiButton > span"
OPP_TYPE_NEXT_BUTTON__SELECTOR = r"#content_581\:0 > div > div > div.inlineFooter > div > button.slds-button.slds-button--neutral.slds-button.slds-button_brand.uiButton"

OPP_GRANT_NEW_HEAD_SELECTOR = r"#content_581\:0 > div > div > div.actionBody > div > article > h2"
OPP_FIELD_DATE_SELECTOR = r"\31 7316\:0 > div > div:nth-child(3) > div.slds-grid.slds-col.slds-is-editing.slds-has-flexi-truncate.pageBlockItemEditWithTooltip.full.forcePageBlockItem.forcePageBlockItemEdit.undo > div > div > div > div > div > div.inputWrapper.slds-grid.slds-grid_vertical-align-center.slds-p-right_x-small > div > div"
OPP_FIELD_STAGE_SELECTOR = r"#\32 1870\:0 > div > a"

# TODO determine if this selector is stable or find another means to select the Edit button
OPP_RECORD_EDIT_BUTTON_SELECTOR = r"#brandBand_1 > div > div.center.oneCenterStage.lafSinglePaneWindowManager > div.windowViewMode-normal.oneContent.active.lafPageHost > div > div.flexipagePage > div > div.row.region-header > div > header > div.slds-page-header.slds-page-header_record-home.s1FixedTop.forceHighlightsStencilDesktop.forceRecordLayout > div > div.slds-col.slds-no-flex.slds-grid.slds-grid_vertical-align-center.actionsContainer > ul > li:nth-child(1) > a > div"

OPP_FORM_SAVE_BUTTON_SELECTOR = r"#\31 4899\:0 > div > div > article > div.riseTransitionEnabled.test-id__inline-edit-record-layout-container.risen > div > div.footer.active > div > div > button.slds-button.slds-button--neutral.uiButton--brand.uiButton.forceActionButton"
## Appears that save botton on edit has different selector
OPP_FORM_EDIT_SAVE_BUTTON_SELECTOR = r"body > div.desktop.container.forceStyle.oneOne.lafStandardLayoutContainer.lafAppLayoutHost.forceAccess.forceStyle.oneOne > div.DESKTOP.uiContainerManager > div.DESKTOP.uiModal--medium.uiModal.forceModal.open.active > div.panel.slds-modal.slds-fade-in-open > div > div.modal-footer.slds-modal__footer > div > button.slds-button.slds-button--neutral.uiButton--default.uiButton--brand.uiButton.forceActionButton"

##########################
