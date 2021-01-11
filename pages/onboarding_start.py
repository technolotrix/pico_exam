from basepage import BasePage
from locators import Onboarding as OBL
from libs.sel.helpers import CustomActions


class OnboardingStartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)

    def is_company_name(self):
        return data.COMPANY_NAME in self.extract_logo_text()

    def is_company_tagline(self):
        return data.TAGLINE in self.extract_tagline_text()

    def is_nav_link_active(self, link):
        print(self.click_link(link), self.get_active_nav_link())
        return self.click_link(link) == self.get_active_nav_link()

    def wait_for_preloader(self):
        self.helpers.wait_for_not_element(TNL.PRELOADER)

    def extract_logo_text(self):
        lt = self.helpers.get_text(
            TNL.LOGO)
        return lt

    def extract_tagline_text(self):
        tt = self.helpers.get_text(
            TNL.TAGLINE)
        return tt

    def click_link(self, linkname):
        links = {
            'faq': TNL.FAQ_LINK,
            'home': TNL.HOME_LINK,
            'contact': TNL.CONTACT_LINK,
            'services': TNL.SERVICES_LINK,
            #'blog': TNL.BLOG_LINK,
            'content': TNL.CONTENT_LINK,
            'about': TNL.ABOUT_LINK
            }

        elem = self.helpers.find_and_click(links.get(linkname))
        self.wait_for_link_scroll(linkname)
        return elem

    def wait_for_link_scroll(self, linkname):
        links = {
            'faq': TNL.FAQ_HEADING,
            'home': TNL.HOME_HEADING,
            'contact': TNL.CONTACT_HEADING,
            'services': TNL.SERVICES_HEADING,
            #'blog': TNL.BLOG_HEADING,
            'content': TNL.CONTENT_HEADING,
            'about': TNL.ABOUT_HEADING
            }

        elem = self.helpers.is_in_view(links.get(linkname))
        return elem

    def get_active_nav_link(self):
        ani = self.helpers.find(TNL.ACTIVE_NAV_ITEM)
        return ani

