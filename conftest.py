import pytest
import Framework.logger as logger
import Framework.testdata as testdata
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.auth_page import AuthPage
from fake_useragent import UserAgent


def pytest_addoption(parser):
    """Запуск тестов без / с headless режимом из строки.
    Дефолтно тесты запускаются в headless режиме.
    """

    parser.addoption('--headless',
                     default='true',
                     help='headless mode')


@pytest.fixture(scope="class")
def browser(request):
    """Инициализация вебдрайвера и опций браузера."""

    options = Options()
    ua = UserAgent(browsers=['chrome'])
    headless = request.config.getoption('--headless')
    if headless == 'true':
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={ua.random}')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_sessionstart(session):
    """Запись сессии тест рана."""

    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Хук для создания отчета."""

    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session):
    """Запись логов в файл."""

    logger.write_logs(str(session.results).replace(', ', '\n'))


@pytest.fixture(scope='session')
def get_test_data():
    """Фикстура для получения тестовых данных.
    Используется единовременно перед началом тестовой сессии в классе TestBase.
    """

    testdata.create_test_data()


@pytest.fixture()
def open_auth_page(browser):
    ap = AuthPage(browser)
    ap.open_auth_page()
