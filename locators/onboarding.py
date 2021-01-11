from selenium.webdriver.common.by import By

print()

class CommonLocators():
    # By.ID is industry best practice,
    # because unique element identifiers are more reliable
    COMPANY_LOGO = (By.CSS_SELECTOR, "div.logo > img")


class OnboardingLocators():
    CLOSE_WIZARD_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) > a > img")
    LOGIN_BUTTON = (By.LINK_TEXT, "Log in.")
    GOOGLE_BUTTON = (By.LINK_TEXT, "Continue with Google")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'")
    COMMUNITY_AGREEMENT = (By.LINK_TEXT, "Pico Community Agreement")


class GoogleSignupLocators():
    CHOOSE_ACCOUNT = (By.LINK_TEXT, "Choose an account")
