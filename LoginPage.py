from PageObjectLibrary import PageObject
from MyUtils import MyUtils


class LoginPage(PageObject):
    PAGE_TITLE = "Extreme Management Center: Login"
    PAGE_URL = "/OneView/home"

    # Page Object Locators
    _locators = {
        "logo":             "class = extrLogoImage",
        "username":         "name = j_username",
        "password":         "name = j_password",
        "submit_button":    "Submit"
    }

    # Business KEYWORDS
    def login_to_emc(self, username, password):
        """Login to Extreme Management Server"""
        # Object
        login_btn = self.browser.find_element_by_css_selector("button[type='%s']" % self.locator.submit_button)

        # Enter username and password
        self.se2lib.input_text(self.locator.username, username)
        #MyUtils.wait_for(1)
        self.se2lib.input_text(self.locator.password, password)
        # Submit the form
        login_btn.click()
        # self.se2lib.open_context_menu(self, self.locator.submit_button)
        # self.logger.info("Login to EMC server - SUCCESS!!!")
