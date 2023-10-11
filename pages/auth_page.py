from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):

    __LOCATOR_BUTTON_AUTH_VK = (By.CSS_SELECTOR, "[data-t='provider:primary:vk']")
    __LOCATOR_BUTTON_ENTER = (By.CSS_SELECTOR, "[id='passp:sign-in']")
    __LOCATOR_BUTTON_MAIL = (By.CSS_SELECTOR, "[data-type='login']")
    __LOCATOR_BUTTON_PHONE = (By.CSS_SELECTOR, "[data-type='phone']")
    __LOCATOR_FIELD_LOGIN_BY_EMAIL = (By.CSS_SELECTOR, "[id='passp-field-login']")
    __LOCATOR_FIELD_LOGIN_BY_PHONE = (By.CSS_SELECTOR, "[id='passp-field-phone']")
    __LOCATOR_FIELD_PASSWORD = (By.CSS_SELECTOR, "[id='passp-field-passwd']")
    __LOCATOR_INPUT_LOGIN_NOTIFICATIONS = (By.CSS_SELECTOR, "[id='field:input-login:hint']")
    __LOCATOR_INPUT_PASSWORD_NOTIFICATIONS = (By.CSS_SELECTOR, "[id='field:input-passwd:hint']")
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

    def click_on_button_enter(self):
        """Нажатие на кнопку "Войти"."""

        self._find_element(self.__LOCATOR_BUTTON_ENTER).click()

    def get_notification_message(self, where):
        """Получение текста уведомления."""

        if where == 'login':
            return (self._find_element(self.__LOCATOR_INPUT_LOGIN_NOTIFICATIONS).get_attribute('innerText').
                    replace(u'\xa0', u' '))
        elif where == 'password':
            return self._find_element(self.__LOCATOR_INPUT_PASSWORD_NOTIFICATIONS).get_attribute('innerText')
        else:
            raise ValueError('Некорректно выбрана локация уведомления.')

    def enter_password(self, password):
        """Ввод пароля."""

        self._enter_value(self.__LOCATOR_FIELD_PASSWORD, password)

    def get_button_mail(self):
        """Возвращает вебэлемент кнопки "Почта".
        Можно использовать в качестве альтернативы методам, типа "click_on_button_enter".
        """

        return self._find_element(self.__LOCATOR_BUTTON_MAIL)

    def get_button_phone(self):
        """Возвращает вебэлемент кнопки "Телефон"."""

        return self._find_element(self.__LOCATOR_BUTTON_PHONE)

    def get_auth_login_field(self, login_by):
        """Возвращает вебэлемент поля для ввода логина.

        :Args:
        - login_by - выбор поля для ввода логина: "логин" или "телефон"
        """

        if login_by == 'login':
            return self._find_element(self.__LOCATOR_FIELD_LOGIN_BY_EMAIL)
        elif login_by == 'phone':
            return self._find_element(self.__LOCATOR_FIELD_LOGIN_BY_PHONE)
        else:
            raise ValueError('Некорректно выбран формат поля.')

    def click_on_button_vk_auth(self):
        """Нажатие на кнопку авторизации через ВК."""

        self._find_element(self.__LOCATOR_BUTTON_AUTH_VK).click()