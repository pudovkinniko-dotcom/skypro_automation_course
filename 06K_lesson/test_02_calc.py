import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Настройка и запуск браузера Google Chrome
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()


def test_slow_calculator(driver):
    # 1. Открыть страницу slow-calculator
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # 2. В поле ввода по локатору #delay ввести значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажать на кнопки:7, +, 8,=
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверить (assert), что в окне отобразился результат 15
    # через 45 секунд
    screen_locator = (By.CLASS_NAME, "screen")

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(screen_locator, "15")
    )

    # Итоговый assert для проверки текста в окне
    result_text = driver.find_element(*screen_locator).text
    assert result_text == "15", f"Ожидается рузультат '15', \
        но отобразилось '{result_text}'"
