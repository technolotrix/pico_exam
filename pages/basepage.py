from libs.selenium_helpers import CustomActions


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)
