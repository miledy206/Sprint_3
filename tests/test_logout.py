from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from data import *


class TestLogout:

    def test_logout_after_success_login(self, run_driver):
        """Проверка кнопки 'Выйти' в личном кабинете"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ButtonsLocators.FIND_LOGIN_BTN_MAIN_PAGE)).click()

        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(email)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        driver.find_element(*ButtonsLocators.FIND_LOGOUT_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.LOGIN_HEADER))

        assert driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE)


