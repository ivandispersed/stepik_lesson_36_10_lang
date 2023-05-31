import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Функция считывания параметра "язык" для теста
def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store', 
        default='en',
        help='Choose language for test'
        )

#Фикстура, запускающая (и закрывающая после теста) браузер и принудительно выставляющая ему язык из ключа теста
@pytest.fixture()
def browser(request):
    forced_language = request.config.getoption("language")
    cur_browser_options = Options()
    cur_browser_options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': forced_language}
    )
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=cur_browser_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
