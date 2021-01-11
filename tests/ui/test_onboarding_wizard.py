from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest

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

    ### Onboarding page tests: Sign up using email ###

    # @attr(priority="hello world")
    # def test_company_logo_is_on_onboarding_page(self):
    #     assert self.page.is_element_on_page('logo')

    # @attr(priority="high")
    # def test_clicking_login_link_directs_user_to_login_page(self):
    #     self.page.click_link_and_wait('log_in')
    #     assert self.page.is_page(onboarding_data.login_url)

    @attr(priority="medium"):
    def test_clicking_x_closes_signup_workflow_and_returns_user_to_main_page(self):
        raise SkipTest("Not implemented")
        # Click x icon
        # Verify url of new page == main page url
        pass

    @attr(priority="critical", keywords=["end to end"])
    def test_user_can_create_new_account_with_valid_email_name_and_password(self):
        raise SkipTest("Blocker: next button is not clickable in selenium")
        # Enter valid email
        email = tools.create_test_email(onboarding_data.valid_email)
        self.page.click_and_fill_out_form('email', email)
        # Click next
        self.page.click_button_and_wait('next')
        # Enter valid name
        # Enter valid password
        name = onboarding_data.valid_name
        password = tools.create_test_password()

        self.page.click_and_fill_out_form('name', name)
        self.page.click_and_fill_out_form('password', password)

        # Click next
        self.page.click_button_and_wait('next')
        # Email verification sent
        assert self.page.is_element_on_page('email_verification')

    @attr(priority="high")
    def test_user_can_click_next_after_entering_valid_email(self):
        # Format the test email str and use it in the form
        email = tools.create_test_email(onboarding_data.valid_email)
        self.page.click_and_fill_out_form('email', email)

        assert self.page.click_button_and_wait('next')

    @attr(priority="high")
    def test_user_cannot_sign_up_with_already_used_email(self):
        # Sign up with workflow using valid inputs to create account
        # Open onboarding wizard and sign up using the same email as step 1
        # Expected behavior: Error message telling user email is taken/used
        raise SkipTest("Blocker: need to verify correct user behavior")

        email = data.onboarding_data.existing_email
        self.page.click_and_fill_out_form('email', email)

        assert self.page.is_correct_text_displayed(
            'existing_email_error_message', 'That email address already exists')

    @attr(priority="high")
    def test_error_appears_if_user_signs_up_with_invalid_email(self):
        raise SkipTest("Blocker: next button is not clickable in selenium")

        for email in onboarding_data.invalid_emails:
            self.page.click_and_fill_out_form('email', email)
            if self.page.is_clickable('next'):
                raise AssertionError('Invalid email {0} failure'.format(email))
            # element.clear() not clearing field, try this:
            self.page.click_and_fill_out_form('email', '')

    @attr(priority="medium")
    def test_next_button_is_unclickable_if_email_is_blank(self):
        email = ''
        self.page.click_and_fill_out_form('email', email)
        assert not self.page.is_clickable('next')

    @attr(priority="low")
    def test_email_field_is_unpopulated_with_placeholder_text_on_pageload(self):
        raise SkipTest("Not implemented")

    @attr(priority="high", keywords=["out of scope"])
    def test_clicking_community_agreement_link_opens_community_agreement_page(self):
        raise SkipTest("Not implemented, out of scope")

    ### Onboarding page tests: Enter Name and Password ###

    @attr(priority="high")
    def test_user_is_prompted_to_enter_a_name_and_password_after_entering_valid_unused_email(self):
        email = tools.create_test_email(onboarding_data.valid_email)
        password = tools.make_valid_password

        self.page.click_and_fill_out_form('email', email)
        self.page.click_button_and_wait('next')

        assert self.page.is_element_on_page('name') and self.page.is_element_on_page('password')

    @attr(priority="high")
    def test_user_is_prompted_to_enter_a_name_after_entering_valid_email(self):
        email = tools.create_test_email(onboarding_data.valid_email)
        name = onboarding_data.valid_name

        self.page.click_and_fill_out_form('email', email)
        self.page.click_button_and_wait('next')
        self.page.click_and_fill_out_form('name', name)

        assert self.page.is_element_on_page('name')

    @attr(priority="high")
    def test_next_button_is_unclickable_if_name_is_blank(self):
        raise SkipTest("Blocker: next button is enabled but not clickable, selector bug")

        email = tools.create_test_email(onboarding_data.valid_email)
        password = tools.create_test_password()

        self.page.click_and_fill_out_form('email', email)
        self.page.click_button_and_wait('next')

        self.page.click_and_fill_out_form('password', password)
        # Wait for page to load and verify 'next' button is unclickable if name is blank
        assert not self.page.click_button_and_wait('next')

    @attr(priority="high")
    def test_next_button_is_unclickable_if_password_is_blank(self):
        raise SkipTest("Next button blocker")

        email = tools.create_test_email(onboarding_data.valid_email)
        name = onboarding_data.valid_name

        self.page.click_and_fill_out_form('email', email)
        self.page.click_button_and_wait('next')

        self.page.click_and_fill_out_form('name', name)

        assert not self.page.click_button_and_wait('next')

    @attr(priority="high")
    def test_next_button_is_unclickable_if_name_and_password_both_blank(self):
        raise SkipTest("Blocker: next button is enabled but not clickable, selector bug")

        email = tools.create_test_email(onboarding_data.valid_email)
        self.page.click_and_fill_out_form('email', email)
        self.page.click_button_and_wait('next')

        assert not self.page.click_button_and_wait('next')
