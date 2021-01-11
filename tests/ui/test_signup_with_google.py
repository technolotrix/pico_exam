from nose.plugins.attrib import attr
from nose.plugins.skip import Skip, SkipTest

from data import onboarding as onboarding_data
from data.urls import onboarding_url as url

from libs import tools
from libs.basedriver import BaseDriver
from pages.onboarding import OnboardingPage


class TestOnboardingWizard():

    @classmethod
    def setUpClass(cls):
        cls.driver = BaseDriver().driver
        cls.page = OnboardingPage(cls.driver)

    def setUp(self):
        if not self.page.is_page(onboarding_data.onboarding_url):
            self.driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    ### Gmail Signup from Onboarding ###

    @attr(priority="high")
    def test_clicking_gmail_signup_causes_gmail_popup_to_appear(self):
        elem = self.page.click_button_and_wait_for_new_window('google_signup')
        text = self.page.extract_element_text('google_signup_window')
        assert elem and (text == 'Sign in with Google')

    ### Fill out other tests using Google Signup workflow as needed in this file ##

    @attr(priority="high")
    def test_user_can_complete_workflow_using_google_signup(self):
        pass
