import pytest
from pages.auth_page import AuthPage


@pytest.mark.usefixtures('browser', 'get_test_data')
class TestBase:

    def setup_method(self):
        """Инициализация классов Page object."""

        self.ap = AuthPage(self.driver)
