import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: es, ru, fr or any other available language on website")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # Chrome options тест
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Firefox options and service
    # Опции для Firefox модифицированны так чтобы браузер смог запускаться на Ubuntu где стоит snap программа.
    # !!!!!!!!!!!!!!!! Внимание запуск Firefox скорее всего не будет работать в Windows and MacOS !!!!!!!!!!!!!!!!!!
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    service = Service(executable_path="/snap/bin/firefox.geckodriver")

    if browser_name == "chrome" and user_language == user_language:
        print("\nstart chrome browser for test.............................................................")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox" and user_language == user_language:
        print("\nstart firefox browser for test..............................................................")
        browser = webdriver.Firefox(options=options_firefox, service=service)
        browser.maximize_window()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox.')
    yield browser
    print("\nquit browser..............................................................................")
    browser.quit()
