import selenium

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.switch_to import SwitchTo

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException as Stale

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.basedriver import WAIT


class CustomActions():

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except (NoSuchElementException, ElementNotVisibleException, Stale) as e:
            return False
        return element

    def find_and_click(self, locator):
        element = self.find(locator)

        if element:
            element.click()
        return element

    def send_keys(self, locator, keys):
        locator = self.find(locator)
        locator.send_keys(keys)

    def get_page_url(self):
        return self.driver.current_url

    def fill_out_form(self, locator, text):
        element = self.find(locator)

        if element:
            element.click()
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        element = self.find(locator)

        if element:
            try:
                text = element.text
            except ElementNotVisibleException:
                return ''
            return text
        return ''

    def wait_for_element(self, locator):
        self.driver.implicitly_wait(3)
        wait = WebDriverWait(self.driver, WAIT)

        try:
            wait.until(lambda s: s.find_element(*locator).is_displayed())
        except (TimeoutException, ElementNotVisibleException, Stale) as e:
            return False
        else:
            return True
        finally:
            self.driver.implicitly_wait(WAIT)

    def wait_for_not_element(self, locator):
        self.driver.implicitly_wait(3)
        wait = WebDriverWait(self.driver, WAIT)

        try:
            wait.until_not(lambda s: s.find_element(*locator).is_displayed())
        except (TimeoutException, ElementNotVisibleException, Stale) as e:
            return False
        else:
            return True
        finally:
            self.driver.implicitly_wait(WAIT)

    def wait_for_enabled_element(self, locator):
        self.driver.implicitly_wait(3)
        wait = WebDriverWait(self.driver, WAIT)

        try:
            wait.until_not(lambda s: s.find_element(*locator).is_enabled())
        except (TimeoutException, ElementNotVisibleException, Stale) as e:
            return False
        else:
            return True
        finally:
            self.driver.implicitly_wait(WAIT)

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_new_window(self, handle):
        return self.driver.switch_to_window(handle)

    def wait_for_element_to_be_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException, ElementNotVisibleException) as e:
            print("Element {0} is not found after wait, so it cannot be clicked. Error message: {1}".format(locator, e))
            return False
        else:
            return True
