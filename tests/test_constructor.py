from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import *


class TestConstructor:

    def test_navigation_inside_constructor_without_login_sauce(self, run_driver):
        """Проверка перехода в подменю 'Соусы' без авторизации"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorNavi.FIND_BUNS))

        driver.find_element(*ConstructorNavi.FIND_SAUCE).click()

        class_of_element = driver.find_element(*ConstructorNavi.SAUCE_HEADER).get_attribute('class')
        assert 'tab_tab_type_current' in class_of_element

    def test_navigation_inside_constructor_without_login_filling(self, run_driver):
        """Проверка перехода в подменю 'Начинки' без авторизации"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorNavi.FIND_BUNS))

        driver.find_element(*ConstructorNavi.FIND_FILLINGS).click()

        class_of_element = driver.find_element(*ConstructorNavi.FILLINGS_HEADER).get_attribute('class')
        assert 'tab_tab_type_current' in class_of_element

    def test_navigation_inside_constructor_without_login_buns(self, run_driver):
        """Проверка перехода в подменю 'Булки' без авторизации"""

        driver = run_driver
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorNavi.FIND_BUNS))

        driver.find_element(*ConstructorNavi.FIND_FILLINGS).click()
        driver.find_element(*ConstructorNavi.FIND_BUNS).click()

        class_of_element = driver.find_element(*ConstructorNavi.BUNS_HEADER).get_attribute('class')
        assert 'tab_tab_type_current' in class_of_element

