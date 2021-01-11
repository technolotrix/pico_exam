from pages.basepage import BasePage
from data.locators import CommonLocators, OnboardingLocators, GoogleSignupLocators, LoginLocators
from libs.selenium_helpers import CustomActions


class OnboardingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)

    def is_company_logo_present(self):
        return self.helpers.find(CommonLocators.COMPANY_LOGO)

    def is_page(self, expected_url):
        return self.helpers.get_page_url() == expected_url

    def is_element_on_page(self, element):
        elems = {
            'email_verification': OnboardingLocators.EMAIL_SENT_VERIFICATION,
            'logo': CommonLocators.COMPANY_LOGO,
            'name': OnboardingLocators.NAME_FIELD,
            'next': OnboardingLocators.NEXT_BUTTON,
            'password': OnboardingLocators.PASSWORD_FIELD,
            }

        elem = elems.get(element)
        return self.helpers.find(elem)

    def is_clickable(self, element):
        elems = {
            'next': OnboardingLocators.NEXT_BUTTON,
            }

        elem = elems.get(element)
        return self.helpers.wait_for_enabled_element(elem)

    def is_correct_text_displayed(self, element, expected_text):
        found_text = self.extract_element_text(element)
        return found_text == expected_text

    def extract_element_text(self, element):
        elements = {
            'google_signup_window': GoogleSignupLocators.SIGN_IN_WITH_GOOGLE,
            'existing_email_error_message': OnboardingLocators.EMAIL_EXISTS_ERROR
            }

        elem = elements.get(element)

        return self.helpers.get_text(elem)

    def click_link_and_wait(self, linkname):
        # Waits for an element on a different page before continuing
        links = {
            'log_in': {
                'click': OnboardingLocators.LOGIN_BUTTON,
                'wait_for': LoginLocators.LOGIN_BUTTON
                },
            }

        l = links.get(linkname)

        elem = self.helpers.find_and_click(l.get('click'))
        wait = self.helpers.wait_for_element(l.get('wait_for'))
        return wait

    def click_button_and_wait(self, button):
        # Waits for an element on same page before continuing
        buttons = {
            'next': {
                'click': OnboardingLocators.NEXT_BUTTON,
                'wait_for': OnboardingLocators.NEXT_BUTTON_DISABLED
            },
        }

        b = buttons.get(button)

        elem = self.helpers.find_and_click(b.get('click'))
        wait = self.helpers.wait_for_element(b.get('wait_for'))
        return wait

    def click_button_and_wait_for_new_window(self, button):
        # Waits for an element in a new window before continuing
        buttons = {
            'google_signup': {
                'click': GoogleSignupLocators.GOOGLE_BUTTON,
                'wait_for': GoogleSignupLocators.SIGN_IN_WITH_GOOGLE
            },
        }

        b = buttons.get(button)

        start_windows = self.helpers.get_window_handles()
        elem = self.helpers.find_and_click(b.get('click'))
        end_windows = self.helpers.get_window_handles()
        new_windows = [window for window in end_windows if window not in start_windows]
        # Todo: clean this up and simplify rather than relying on indices
        self.helpers.switch_to_new_window(new_windows[0])
        wait = self.helpers.wait_for_element(b.get('wait_for'))
        return wait

    def click_and_fill_out_form(self, fieldname, data):
        fields = {
            'email': {
                'click': OnboardingLocators.EMAIL_FIELD,
                },
            'name': {
                'click': OnboardingLocators.NAME_FIELD,
                },
            'password': {
                'click': OnboardingLocators.PASSWORD_FIELD,
                }
            }

        f = fields.get(fieldname)
        self.helpers.fill_out_form(f.get('click'), data)
