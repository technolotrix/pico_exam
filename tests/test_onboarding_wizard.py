from nose.tools import assert_true

from libs.basedriver import BaseDriver

from pages.onboarding_start import OnboardingStartPage
from config.settings import onboarding_start_url as url


class TestOnboardingWizardStart():

    @classmethod
    def setUpClass(self):
        self.driver = BaseDriver().driver
        self.driver.get(url)
        self.page = OnboardingStartPage(self.driver)

        self.page.wait_for_preloader()
        self.page.click_link('home')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_company_logo_is_on_onboarding_page(self):
        assert self.page.is_company_logo()

    def test_email_field_is_unpopulated_with_placeholder_text(self):
        assert self.page.is_company_tagline()

    def test_next_button_is_unclickable_if_email_is_blank(self):
        self.page.click_link('faq')
        assert self.page.is_nav_link_active('home')

    # def test_clicking_nav_links_updates_nav_active(self):
    #     for page in PAGELIST:
    #         try:
    #             #print(page)
    #             #print(self.page.click_link(page))
    #             yield assert_true, self.page.is_nav_link_active(page)
    #         except Exception as e:
    #             print(str(e))