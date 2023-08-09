from selenium.webdriver.common.by import By


class ButtonsLocators:
    FIND_LOGIN_BTN_MAIN_PAGE = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    FIND_LOGIN_BTN_LOGIN_PAGE = (By.XPATH, './/button[text() = "Войти"]')
    FIND_LOGIN_LINK = (By.XPATH, './/a[text() = "Войти"]')
    FIND_REGISTRATION_LINK = (By.XPATH, './/a[text() = "Зарегистрироваться"]')
    FIND_REGISTRATION_BTN = (By.XPATH, './/button[text() = "Зарегистрироваться"]')
    FIND_PROFILE_BTN = (By.XPATH, './/p[text() = "Личный Кабинет"]')
    FIND_RECOVER_PASS_LINK = (By.XPATH, './/a[text() = "Восстановить пароль"]')
    FIND_LOGOUT_BTN = (By.XPATH, './/button[text() = "Выход"]')


class PersonalDataLocators:
    FIND_NAME_FIELD = (By.XPATH, './/label[text() = "Имя"]/parent::div/input')
    FIND_EMAIL_FIELD = (By.XPATH, './/label[text() = "Email"]/parent::div/input')
    FIND_PASSWORD_FIELD = (By.XPATH, './/label[text() = "Пароль"]/parent::div/input')
    FIND_LOGIN_FIELD = (By.XPATH, './/label[text() = "Логин"]/parent::div/input')


class HelpingTexts:
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, './/p[text() = "Некорректный пароль"]')
    LOGIN_HEADER = (By.XPATH, './/h2[text() = "Вход"]')
    PROFILE_LINK = (By.XPATH, './/a[text() = "Профиль"]')
    CONSTRUCTOR_LINK = (By.XPATH, './/p[text() = "Конструктор"]')
    MAKE_BURGER = (By.XPATH, './/h1[text() = "Соберите бургер"]')
    RECOVER_HEADER = (By.XPATH, './/h2[text() = "Восстановление пароля"]')
    NAME_FIELD = (By.XPATH, './/label[text() = "Имя"]')


class ConstructorNavi:
    FIND_FILLINGS = (By.XPATH, './/span[text() = "Начинки"]')
    FIND_BUNS = (By.XPATH, './/span[text() = "Булки"]')
    FIND_SAUCE = (By.XPATH, './/span[text() = "Соусы"]')
    FILLINGS_HEADER = (By.XPATH, './/span[text() = "Начинки"]/parent::div')
    BUNS_HEADER = (By.XPATH, './/span[text() = "Булки"]/parent::div')
    SAUCE_HEADER = (By.XPATH, './/span[text() = "Соусы"]/parent::div')
