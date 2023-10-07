from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        """Инициализация вебдрайвера."""

        self.driver = driver

    def _find_element(self, locator, time=2.5):
        """Поиск вебэлемента на странице. Возвращает первый найденный элемент."""

        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by {locator}")

    def _find_elements(self, locator, time=2.5):
        """Поиск вебэлементов на странице. Возвращает список вебэлементов."""

        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by {locator}")

    def _enter_value(self, field_locator, value):
        """Ввод значения в поле."""

        field = self._find_element(field_locator)
        field.click()
        field.clear()
        field.send_keys(value)


