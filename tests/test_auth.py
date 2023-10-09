import time
from tests.test_base import TestBase


class TestAuth(TestBase):

    def test_auth(self):

        self.ap.open_auth_page()
        self.ap.click_on_button_mail()
        self.ap.enter_login('login', 'asd;laksd')
        time.sleep(3)

    def test_bar(self):

        self.ap.open_auth_page()
        self.ap.click_on_button_mail()
        self.ap.enter_login('login', 'asd;laksd')
        time.sleep(3)