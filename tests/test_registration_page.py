from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from helper import *
from locators import *


class TestRegistration:

    def test_registration_correct_data(self, run_driver):
        """Позитивная проверка на регистрацию пользователя"""

        correct_login = generation_correct_email()
        correct_password = generation_correct_password()

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ButtonsLocators.FIND_LOGIN_BTN_MAIN_PAGE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ButtonsLocators.FIND_REGISTRATION_LINK)).click()

        driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).send_keys(name)
        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(correct_login)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(correct_password)

        driver.find_element(*ButtonsLocators.FIND_REGISTRATION_BTN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            HelpingTexts.LOGIN_HEADER))

        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(correct_login)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(correct_password)

        driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        check_value = driver.find_element(*PersonalDataLocators.FIND_LOGIN_FIELD).get_attribute(
            'value')
        assert check_value == correct_login

    def test_registration_too_short_password(self, run_driver):
        """Негативная проверка на регистрацию пользователя: некорректный пароль"""

        correct_login = generation_correct_email()
        incorrect_password = generation_incorrect_password()

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ButtonsLocators.FIND_LOGIN_BTN_MAIN_PAGE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ButtonsLocators.FIND_REGISTRATION_LINK)).click()

        driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).send_keys(name)
        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(correct_login)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(incorrect_password)

        driver.find_element(*ButtonsLocators.FIND_REGISTRATION_BTN).click()

        WebDriverWait(driver, 3)

        assert driver.find_element(*HelpingTexts.INCORRECT_PASSWORD_MESSAGE)
