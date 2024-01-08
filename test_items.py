import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    # Разкоментировать строку ниже для проверки работоспособности кода. Для запуска теста с параметром "--language=fr"
    # time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    assert button.is_displayed(), "Кнопка не найдена на странице"


