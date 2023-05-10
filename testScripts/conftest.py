import json
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# To Run parallel execution
# pip install pytest-xdist


@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()



@pytest.fixture(scope="class")
def browser_cls(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser")


@pytest.fixture()
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    return params


@pytest.fixture()
def multiple_browser(request, params):
    web_driver = ""
    if params['browser'] == 'chrome':
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    if params['browser'] == 'firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.instance.driver = web_driver
    yield web_driver
    web_driver.close()


@pytest.fixture()
def jsonData():
    with open('testData/testData.json') as config_file:
        data = json.load(config_file)
    return data