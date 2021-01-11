from selenium.webdriver.common.by import By


class CommonLocators():
    # By.ID is industry best practice
    # By.CSS is preferable over xpath and classname (which is not unique)
    COMPANY_LOGO = (By.CSS_SELECTOR, "div[class='logo'] > img")


class OnboardingLocators():

    CLOSE_WIZARD_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) > a > img")
    COMMUNITY_AGREEMENT = (By.LINK_TEXT, "Pico Community Agreement")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    EMAIL_DISPLAY = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > div > form > div > div > div._372002a.col-12 > div")
    EMAIL_SENT_VERIFICATION = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > form > div > div > div._431cfea.col-12 > img")
    INVALID_EMAIL_ERROR = (By.CSS_SELECTOR, "span:contains('Invalid Email'")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > div > form > div > div > div._372002a.col-12 > h4 > a")
    NAME_FIELD = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > div > form > div > div > div._431cfea.col-12 > div:nth-child(1) > div.FormInput-module_container__ll_c1.FormInput-module_error__125Gq > input")
    NEXT_BUTTON = (By.CLASS_NAME, "Button-module_button__3M3oN Button-module_primary__gfhd3")
    NEXT_BUTTON_DISABLED = (By.CLASS_NAME, "Button-module_disabled__3y46V")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password'")
    PASSWORD_STRENGTH = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > div > form > div > div > div._431cfea.col-12 > div:nth-child(3) > div.ProgressBar-module_progressStatus__3ToYl > span:nth-child(1)")

class GoogleSignupLocators():
    GOOGLE_BUTTON = (By.CSS_SELECTOR, "#OnboardingWizard > div.box-dialog > div > div > form > div > div > div._431cfea.col-12 > div.Button-module_buttonWrapper__2hsPF._813abbc > button > div > svg")
    SIGN_IN_WITH_GOOGLE = (By.CLASS_NAME, "kHn9Lb")


# Ideally Login has its own separate file for scalability
class LoginLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#root > div > div.ui.grid.Login > div > div.column.Login-FormContainer.FlexContainer_rowCentered > div.Login-FormContainer-Form > form > div:nth-child(4) > button')


