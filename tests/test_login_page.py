from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_correct_data_via_login_btn(self, login_correct_email, login_correct_pass):
        """Позитивная проверка на авторизацию с помощью кнопки 'Войти в аккаунт' на главной странице"""

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

        check_value = driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').get_attribute(
            'value')
        assert check_value == 'Олеся'

        driver.quit()

    def test_login_correct_data_via_profile(self, login_correct_email, login_correct_pass):
        """Позитивная проверка на авторизацию через переход в меню 'Личный кабинет' на главной странице"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text() = "Личный Кабинет"]'))).click()

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver,3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text() = "Профиль"]')))

        check_value = driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').get_attribute('value')

        assert check_value == 'Олеся'

        driver.quit()

    def test_login_correct_data_via_restore_password(self, login_correct_email, login_correct_pass):
        """Позитивная проверка на авторизацию через восстановление пароля"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text() = "Личный Кабинет"]'))).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text() = "Вход"]')))

        driver.find_element(By.XPATH, './/a[text() = "Восстановить пароль"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text() = "Восстановление пароля"]')))

        driver.find_element(By.XPATH, './/a[text() = "Войти"]').click()

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/label[text() = "Имя"]')))

        check_value = driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').get_attribute('value')

        assert check_value == 'Олеся'

        driver.quit()

    def test_login_correct_data_via_registration(self, login_correct_email, login_correct_pass):
        """Позитивная проверка на авторизацию через страницу регистрации"""

        self.login = login_correct_email
        self.password = login_correct_pass

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, './/button[text() = "Войти в аккаунт"]'))).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, './/a[text() = "Зарегистрироваться"]'))).click()

        driver.find_element(By.XPATH, './/a[text() = "Войти"]').click()

        driver.find_element(By.XPATH, './/label[text() = "Email"]/parent::div/input').send_keys(self.login)
        driver.find_element(By.XPATH, './/label[text() = "Пароль"]/parent::div/input').send_keys(self.password)

        driver.find_element(By.XPATH, './/button[text() = "Войти"]').click()

        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/a[text() = "Профиль"]')))

        check_value = driver.find_element(By.XPATH, './/label[text() = "Имя"]/parent::div/input').get_attribute('value')

        assert check_value == 'Олеся'

        driver.quit()
