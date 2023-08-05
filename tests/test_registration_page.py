from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    name = 'Олеся'

    def test_registration_correct_data(self, generation_correct_email, generation_correct_password):
        """Позитивная проверка на регистрацию пользователя"""

        self.login = generation_correct_email
        self.password = generation_correct_password

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, './/button[text() = "Войти в аккаунт"]'))).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, './/a[text() = "Зарегистрироваться"]'))).click()

        driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').send_keys(self.name)
        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Зарегистрироваться"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h2[text() = "Вход"]')))

        assert driver.find_element(By.XPATH, './/button[text() = "Войти"]')

        driver.quit()

    def test_registration_too_short_password(self, generation_correct_email, generation_incorrect_password):
        """Негативная проверка на регистрацию пользователя: некорректный пароль"""

        self.login = generation_correct_email
        self.password = generation_incorrect_password

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, './/button[text() = "Войти в аккаунт"]'))).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, './/a[text() = "Зарегистрироваться"]'))).click()

        driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').send_keys(self.name)
        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Зарегистрироваться"]').click()

        WebDriverWait(driver, 3)

        assert driver.find_element(By.XPATH, './/p[text() = "Некорректный пароль"]')

        driver.quit()
