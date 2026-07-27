import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    # Настройка и запуск браузера Edge
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()


def test_data_types_form(driver):
    # 1. Открыть страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Явное ожидание (WebDriverWait) для первой загрузки формы
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # 2. Заполнить форму значениями
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

    # Поле Zip code оставляем пустым, как указано в задании
    driver.find_element(By.NAME, "zip-code").clear()

    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # 3. Нажать кнопку Submit
    # Находим кнопку Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Скроллим к ней, чтобы она стала видимой
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    # Кликаем по ней
    submit_button.click()

    # 4. Проверить, что поле Zip code подсвечено красным
    # (класс 'alert-danger')
    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class"), \
        "Поле Zip code должно быть подсвечено красным"

    # 5. Проверить, что остальные поля подсвечены зеленым
    # (класс 'alert-success')
    green_fields_locators = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields_locators:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} должно быть подсвечено зеленым"
