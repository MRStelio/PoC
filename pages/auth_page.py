from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):

    __LOCATOR_BUTTON_ENTER = (By.CSS_SELECTOR, "[id='passp:sign-in']")
    __LOCATOR_BUTTON_MAIL = (By.CSS_SELECTOR, "[data-type='login']")
    __LOCATOR_BUTTON_PHONE = (By.CSS_SELECTOR, "[data-type='phone']")
    __LOCATOR_FIELD_LOGIN_BY_EMAIL = (By.CSS_SELECTOR, "[id='passp-field-login']")
    __LOCATOR_FIELD_LOGIN_BY_PHONE = (By.CSS_SELECTOR, "[id='passp-field-phone']")
    __URL_AUTH_PAGE = 'https://passport.yandex.ru/auth'

    def open_auth_page(self):
        """Открытие страницы авторизации."""

        self.driver.get(self.__URL_AUTH_PAGE)

    def enter_login(self, auth_by, login):
        """Ввод логина или номера телефона.

        :Args:
        - auth_by - выбор поля для ввода логина: "логин" или "телефон"
        - login - логин.
        """

        if auth_by == 'login':
            self._enter_value(self.__LOCATOR_FIELD_LOGIN_BY_EMAIL, login)
        elif auth_by == 'phone':
            self._enter_value(self.__LOCATOR_FIELD_LOGIN_BY_PHONE, login)
        else:
            raise ValueError('Некорректно выбран формат поля.')

    def click_on_button_mail(self):
        """Нажатие на кнопку "Почта"."""

        self._find_element(self.__LOCATOR_BUTTON_MAIL).click()

