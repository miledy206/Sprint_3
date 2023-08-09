from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import *
from data import *


class TestLogin:

    def test_login_correct_data_via_login_btn(self, run_driver):
        """Позитивная проверка на авторизацию с помощью кнопки 'Войти в аккаунт' на главной странице"""

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

    def test_login_correct_data_via_profile(self, run_driver):
        """Позитивная проверка на авторизацию через переход в меню 'Личный кабинет' на главной странице"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.FIND_PROFILE_BTN)).click()

        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(email)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        check_value = driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).get_attribute('value')
        assert check_value == name

    def test_login_correct_data_via_restore_password(self,run_driver):
        """Позитивная проверка на авторизацию через восстановление пароля"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ButtonsLocators.FIND_PROFILE_BTN)).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.LOGIN_HEADER))

        driver.find_element(*ButtonsLocators.FIND_RECOVER_PASS_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.RECOVER_HEADER))

        driver.find_element(*ButtonsLocators.FIND_LOGIN_LINK).click()

        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(email)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.NAME_FIELD))

        check_value = driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).get_attribute('value')

        assert check_value == name

    def test_login_correct_data_via_registration(self, run_driver):
        """Позитивная проверка на авторизацию через страницу регистрации"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ButtonsLocators.FIND_LOGIN_BTN_MAIN_PAGE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ButtonsLocators.FIND_REGISTRATION_LINK)).click()

        driver.find_element(*ButtonsLocators.FIND_LOGIN_LINK).click()

        driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(email)
        driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(password)

        driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        check_value = driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).get_attribute('value')

        assert check_value == name

