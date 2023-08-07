import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import *
from tests.data import *


@pytest.fixture(scope="function")
def run_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def success_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        ButtonsLocators.FIND_LOGIN_BTN_MAIN_PAGE)).click()

    driver.find_element(*PersonalDataLocators.FIND_EMAIL_FIELD).send_keys(email)
    driver.find_element(*PersonalDataLocators.FIND_PASSWORD_FIELD).send_keys(password)

    driver.find_element(*ButtonsLocators.FIND_LOGIN_BTN_LOGIN_PAGE).click()
    yield driver
    driver.quit()
