from selenium.webdriver.common.by import By


class CommonLocators():
    # By.ID is industry best practice,
    # because unique element identifiers are more reliable
    COMPANY_LOGO = (By.CSS, "div.logo > img")


class OnboardingLocators():
    CLOSE_WIZARD_BUTTON = (By.CSS, "div:nth-child(2) > a > img")
    LOGIN_BUTTON = (By.TEXT, "Log in.")
    GOOGLE_BUTTON = (By.TEXT, "Continue with Google")
    EMAIL_FIELD = (By.CSS, "input[type='email']")
    SUBMIT_BUTTON = (By.CSS, "button[type='submit'")
    COMMUNITY_AGREEMENT = (By.TEXT, "Pico Community Agreement")


class GoogleSignupLocators():
    CHOOSE_ACCOUNT = (By.TEXT, "Choose an account")