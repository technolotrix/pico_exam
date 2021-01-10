from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from data import settings

COMMAND_EXECUTOR = 'http://hub:4444/wd/hub'
VALID_BROWSERS = ("chrome", "firefox", "phantomjs")
SIZE = (1200, 1080)
WAIT = 3


class BaseDriver():

    def __init__(self):
        self.browser = settings.BROWSER
        self.run_local = settings.LOCAL_SELENIUM

        if self.browser not in VALID_BROWSERS:
            raise Exception(
                "Invalid browser!  Allowed types are {0}".format(VALID_BROWSERS))

        self.make_driver(self.browser)

    def make_local_driver(self, browser):
        drivers = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome,
            'phantomjs': webdriver.PhantomJS
            }

        return drivers.get(browser)()

    def make_remote_driver(self, browser):
        # For illustrative purposes only
        # Can DRY more
        drivers = {
            'firefox': {
                'desired_capabilities': DesiredCapabilities.FIREFOX,
                },
            'chrome': {
                'desired_capabilities': DesiredCapabilities.CHROME,
                },
            'phantomjs': {
                'desired_capabilities': DesiredCapabilities.PHANTOMJS,
                }
            }

        driver = drivers.get(browser)
        driver['command_executor'] = COMMAND_EXECUTOR

        return webdriver.Remote(driver)

    def set_window_size(self, wait=WAIT, size=None):
        self.driver.implicitly_wait(WAIT)
        if size and isinstance(size, tuple):
            self.driver.set_window_size(size)

    def make_driver(self, browser, size=None):
        if self.run_local:
            self.driver = self.make_local_driver(browser)
        else:
            self.driver = self.make_remote_driver(browser)

        self.set_window_size()
