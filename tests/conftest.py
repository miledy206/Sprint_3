import random
import pytest
import string

@pytest.fixture
def generation_correct_password():
    """Генератор простого пароля с цифрами и буквами на 13 символов"""
    line = string.ascii_letters + string.digits
    passw = ''
    for i in range(12):
        passw = passw + random.choice(line)
    return passw

@pytest.fixture
def generation_incorrect_password():
    """Генератор простого пароля с цифрами и буквами на 4 символов"""
    line = string.ascii_letters + string.digits
    passw = ''
    for i in range(3):
        passw = passw + random.choice(line)
    return passw

@pytest.fixture
def generation_correct_email():
    """Генератор email согласно маске для кейсов регистрации"""
    login = 'safronova_olesia_12_' + str(random.randint(100, 999)) + '@ya.ru'
    return login

@pytest.fixture
def login_correct_email():
    """Созданный заранее и зарегистрированный тестовый пользователь"""
    login = 'safronova_olesya_12_123@ya.ru'
    return login

@pytest.fixture
def login_correct_pass():
    """Созданный заранее и зарегистрированный тестовый пользователь"""
    passw = 'Yandex1234'
    return passw
