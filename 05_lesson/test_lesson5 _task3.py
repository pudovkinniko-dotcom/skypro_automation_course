from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # 1. Найдите все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверьте, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # 3. Проверьте, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed(), (f"Ссылка {link.text}"
                                     f"не отображается на странице")

    # 4. Проверьте, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, (f"Текст первой ссылки"
                                    f"('{first_link_text}') не содержит '1'")

    driver.quit()
