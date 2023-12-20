from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # Заполняем поле Имя
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("FirstName")
    # Заполняем поле Фамилию
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("LastName")
    # Заполняем поле email
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("email@test.qa")
    # Заполняем поле номер телефона
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("+1456987456")
    # Заполняем поле почтового адреса
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("1st street, Test City, 98765")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

