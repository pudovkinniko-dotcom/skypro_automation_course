from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Откройте главную страницу
    driver.get("https://httpbin.org")
    sleep(2)

    # 2. Найдите ссылку по её адресу href и кликните
    html_form_link = driver.find_element(
        By.XPATH, "//a[contains(@href, '/forms/post')]"
    )
    html_form_link.click()
    sleep(2)

    # 3. Проверьте, что URL изменился на /forms/post
    assert ("/forms/post"
            in driver.current_url), "URL не изменился на /forms/post"

    # 4. Вернитесь назад на главную страницу
    driver.back()
    sleep(2)

    # 5. Проверьте, что вернулись на исходный URL
    assert (
        driver.current_url == "https://httpbin.org/"
    ), "Не удалось вернуться на исходный URL"

    driver.quit()
