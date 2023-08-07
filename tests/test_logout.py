from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import *
from tests.locators import *


class TestLogout:

    def test_logout_after_success_login(self, success_login):
        """Проверка кнопки 'Выйти' в личном кабинете"""

        driver = success_login

        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        driver.find_element(*ButtonsLocators.FIND_LOGOUT_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.LOGIN_HEADER))

        assert driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE)


