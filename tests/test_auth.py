import pytest
from Framework.testdata import test_users
from tests.test_base import TestBase


class TestAuth(TestBase):

    @pytest.mark.usefixtures('open_auth_page')
    @pytest.mark.parametrize('invalid_login, notification_message',
                             [(test_users[1]['login'], 'Такой логин не подойдет')])
    def test_invalid_login(self, invalid_login, notification_message):

        url_before = self.ap.driver.current_url
        self.ap.click_on_button_mail()
        self.ap.enter_login('login', invalid_login)
        self.ap.click_on_button_enter()
        notification = self.ap.get_notification_message('login')
        assert notification == notification_message
        url_after = self.ap.driver.current_url
        assert url_before == url_after

    @pytest.mark.usefixtures('open_auth_page')
    @pytest.mark.parametrize('valid_login, invalid_password, notification_message',
                             [('testauth3', test_users[7]['password'], 'Неверный пароль')])
    def test_invalid_password(self, valid_login, notification_message, invalid_password):

        self.ap.click_on_button_mail()
        self.ap.enter_login('login', valid_login)
        self.ap.click_on_button_enter()
        self.ap.enter_password(invalid_password)
        url_before = self.ap.driver.current_url
        self.ap.click_on_button_enter()
        notification = self.ap.get_notification_message('password')
        assert notification == notification_message
        url_after = self.ap.driver.current_url
        assert url_before == url_after

    @pytest.mark.usefixtures('open_auth_page')
    @pytest.mark.parametrize('valid_login, valid_password, welcome_url',
                             [('testauth3', 'rFMTqMmcR', 'https://passport.yandex.ru/auth/welcome')])
    def test_valid_auth_by_login(self, valid_login, valid_password, welcome_url):
        self.ap.click_on_button_mail()
        self.ap.enter_login('login', valid_login)
        self.ap.click_on_button_enter()
        self.ap.enter_password(valid_password)
        self.ap.click_on_button_enter()
        current_url = self.ap.driver.current_url
        assert current_url == welcome_url

    @pytest.mark.usefixtures('open_auth_page')
    @pytest.mark.parametrize('placeholder_login, placeholder_phone',
                             [('Логин или email', '+7')])
    def test_switch_buttons_mail_and_phone(self, placeholder_login, placeholder_phone):

        button_mail = self.ap.get_button_mail()
        button_phone = self.ap.get_button_phone()
        login_field_by_mail = self.ap.get_auth_login_field('login')
        button_mail.click()
        assert login_field_by_mail.get_attribute('placeholder') == placeholder_login
        button_phone.click()
        login_field_by_phone = self.ap.get_auth_login_field('phone')
        assert login_field_by_phone.get_attribute('value') == placeholder_phone

    @pytest.mark.usefixtures('open_auth_page')
    @pytest.mark.parametrize('url_aut_vk', ['social.yandex.ru'])
    def test_auth_by_vk(self, url_aut_vk):

        self.ap.click_on_button_vk_auth()
        self.ap.switch_window(1)
        current_url = self.ap.driver.current_url
        assert url_aut_vk in current_url
