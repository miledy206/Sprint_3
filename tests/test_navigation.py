from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestNavigation:

    def test_navigation_from_profile_to_constructor(self, login_correct_email, login_correct_pass):
        """Проверка перехода из личного кабинета на страницу конструктора"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        click_on_login = driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]')
        driver.execute_script("arguments[0].click();", click_on_login)

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text() = "Профиль"]')))

        driver.find_element(By.XPATH, './/p[text() = "Конструктор"]').click()

        assert driver.find_element(By.XPATH, './/h1[text() = "Соберите бургер"]')

        driver.quit()

    def test_navigation_from_constructor_to_profile(self, login_correct_email, login_correct_pass):
        """Проверка перехода со страницы конструктора в личный кабинет"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        click_on_login = driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]')
        driver.execute_script("arguments[0].click();", click_on_login)

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text() = "Профиль"]')))

        check_value = driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').get_attribute(
            'value')
        assert check_value == 'Олеся'

        driver.quit()
