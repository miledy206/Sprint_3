from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import *
from tests.data import *


class TestNavigation:

    def test_navigation_from_profile_to_constructor(self, success_login):
        """Проверка перехода из личного кабинета на страницу конструктора"""

        driver = success_login
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        driver.find_element(*HelpingTexts.CONSTRUCTOR_LINK).click()

        assert driver.find_element(*HelpingTexts.MAKE_BURGER)

    def test_navigation_from_constructor_to_profile(self, success_login):
        """Проверка перехода со страницы конструктора в личный кабинет"""

        driver = success_login
        driver.find_element(*ButtonsLocators.FIND_PROFILE_BTN).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(HelpingTexts.PROFILE_LINK))

        check_value = driver.find_element(*PersonalDataLocators.FIND_NAME_FIELD).get_attribute(
            'value')
        assert check_value == name
