import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome options тест
options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
options.add_argument(f"--lang={user_language}")

# Firefox options and service
options_firefox = OptionsFirefox()
options_firefox.set_preference("intl.accept_languages", user_language)
service = Service(executable_path="/snap/bin/firefox.geckodriver")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test../////////////////////////////////////////////////////////////////////")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..///////////////////////////////////////////////////////////////////")
        browser = webdriver.Firefox(options=options_firefox, service=service)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser../////////////////////////////////////////////////////////////////////////////////")
    browser.quit()
