import pytest
import Framework.logger as logger
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


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
    headless = request.config.getoption('--headless')
    if headless == 'true':
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
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
