from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from data import *


class TestNavigation:

    def test_navigation_from_profile_to_constructor(self, run_driver):
        """Проверка перехода из личного кабинета на страницу конструктора"""

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

        driver.find_element(*HelpingTexts.CONSTRUCTOR_LINK).click()

        assert driver.find_element(*HelpingTexts.MAKE_BURGER)

    def test_navigation_from_constructor_to_profile(self, run_driver):
        """Проверка перехода со страницы конструктора в личный кабинет"""

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

        check_value = driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).get_attribute(
            'value')
        assert check_value == name
