from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:

    def test_logout_after_success_login(self, login_correct_email, login_correct_pass):
        """Проверка кнопки 'Выйти' в личном кабинете"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, './/button[text() = "Войти в аккаунт"]'))).click()

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text() = "Профиль"]')))

        driver.find_element(By.XPATH, './/button[text() = "Выход"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text() = "Вход"]')))

        assert driver.find_element(By.XPATH, './/button[text() = "Войти"]')

        driver.quit()

