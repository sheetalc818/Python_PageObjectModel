class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_textbox = self.driver.find_element_by_id(self.textbox_username_id)
        username_textbox.clear()
        username_textbox.send_keys(username)

    def set_password(self, password):
        password_textbox = self.driver.find_element_by_id(self.textbox_password_id)
        password_textbox.clear()
        password_textbox.send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()
