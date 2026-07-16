import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_shop(driver):
    # 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизоваться как standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавить в корзину указанные товары
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполнить форму своими данными
    driver.find_element(By.ID, "first-name").send_keys("Nikolay")
    driver.find_element(By.ID, "last-name").send_keys("Pudovkin")
    driver.find_element(By.ID, "postal-code").send_keys("445146")

    # 7. Нажать кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитать со страницы итоговую стоимость (Total)
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # 9. Проверить, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", (
        f"Ожидалась сумма 'Total: $58.29', но получено '{total_text}'"
    )
