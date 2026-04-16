import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEventsPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.greencity.cx.ua/#/greenCity/events"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    #  Тест 1: Відкриття сторінки
    def test_open_events_page(self):
        # Очікуємо появу списку подій
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )
        self.assertTrue(len(events) > 0, "Сторінка не завантажилась або немає елементів")

    # Тест 2: Перевірка наявності подій
    def test_events_are_displayed(self):
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )
        self.assertGreater(len(events), 0, "Події не відображаються")

    #  Тест 3: Клік по події
    def test_open_event_details(self):
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
        )

        events[0].click()

        # перевірка що сторінка змінилась (URL)
        self.wait.until(EC.url_changes(self.url))

        current_url = self.driver.current_url
        self.assertNotEqual(current_url, self.url, "Сторінка події не відкрилась")


if __name__ == "__main__":
    unittest.main()
