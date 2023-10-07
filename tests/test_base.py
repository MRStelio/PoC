import pytest
from pages.auth_page import AuthPage


@pytest.mark.usefixtures('browser')
class TestBase:

    def setup_method(self):

        self.ap = AuthPage(self.driver)
