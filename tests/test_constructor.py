from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    def test_navigation_inside_constructor_without_login_sauce(self):
        """Проверка перехода в подменю 'Соусы' без авторизации"""

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/span[text() = "Булки"]')))

        driver.find_element(By.XPATH, './/span[text() = "Соусы"]').click()

        assert driver.find_element(By.XPATH, './/h2[text() = "Соусы"]')

        driver.quit()

    def test_navigation_inside_constructor_without_login_filling(self):
        """Проверка перехода в подменю 'Начинки' без авторизации"""

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/span[text() = "Булки"]')))

        driver.find_element(By.XPATH, './/span[text() = "Начинки"]').click()

        assert driver.find_element(By.XPATH, './/h2[text() = "Начинки"]')

        driver.quit()

    def test_navigation_inside_constructor_without_login_buns(self):
        """Проверка перехода в подменю 'Булки' без авторизации"""

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/span[text() = "Булки"]')))

        driver.find_element(By.XPATH, './/span[text() = "Начинки"]').click()
        driver.find_element(By.XPATH, './/span[text() = "Булки"]').click()

        assert driver.find_element(By.XPATH, './/h2[text() = "Булки"]')

        driver.quit()

