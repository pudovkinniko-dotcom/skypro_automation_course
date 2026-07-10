import time
from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Сначала обязательно открываем сайт
    driver.get("https://gitflic.ru")

    # Сначала СОЗДАЕМ переменные
    cookie_user_1 = {
        "name": "SESSION",
        "value": "N2U4YjMwZjktOTMyOC00Y2FiLThlMGYtZTNiMGViOGM1NjYz"
    }
    cookie_user_2 = {
        "name": "SESSION",
        "value": "N2U4YjMwZjktOTMyOC00Y2FiLThlMGYtZTNiMGViOGM1NjYz"
    }
    # 2. Устанавливаем cookie пользователя 1
    driver.add_cookie(cookie_user_1)

    # 3. Обновляем страницу, чтобы применилась авторизация
    driver.refresh()

    # 4. Переходим на страницу профиля пользователя 1
    driver.get("https://gitflic.ru/user/23323")
    time.sleep(2)  # Небольшая пауза, чтобы редирект успел отработать

    # 5. Сохраняем текущий URL профиля первого пользователя
    url_user_1 = driver.current_url

    # 6. Разлогиниваемся (полностью очищаем куки)
    driver.delete_all_cookies()

    # 7. Устанавливаем cookie пользователя 2
    driver.get("https://gitflic.ru")
    driver.add_cookie(cookie_user_2)

    # 8. Обновляем страницу
    driver.refresh()

    # 9. Переходим на страницу профиля пользователя 2
    driver.get("https://gitflic.ru/user/7835493")
    time.sleep(2)

    # 10. Сохраняем текущий URL профиля второго пользователя
    url_user_2 = driver.current_url

    # 11. Проверяем, что URL для пользователя 1 и пользователя 2 различаются
    assert (
            url_user_1 != url_user_2
    ), (f"Ошибка: оба профиля ведут на один URL '{url_user_1}'."
        f"Проверьте валидность кук.")

    print(f"\nURL Пользователя 1: {url_user_1}")
    print(f"URL Пользователя 2: {url_user_2}")

    driver.quit()
