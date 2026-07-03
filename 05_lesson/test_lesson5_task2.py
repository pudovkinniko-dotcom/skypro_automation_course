from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # 1. Найдите поле ввода с названием custname
    name_field = driver.find_element(By.NAME, "custname")

    # 2. Введите в него ваше имя
    name_field.send_keys("Nikolay")

    # 3. Найдите кнопку Submit и нажмите на нее
    submit_button = (driver.find_element
                     (By.XPATH, "//button[text()='Submit order']"))
    submit_button.click()
    sleep(5)

    # 4. Проверьте, что после нажатия URL изменился
    # После отправки формы URL должен поменяться на https://httpbin.org
    assert (
            driver.current_url != "https://httpbin.org/forms/post"
    ), "URL не изменился после отправки формы"
    assert (
            "/post" in driver.current_url
    ), "Форма не была отправлена на эндпоинт /post"

    driver.quit()
