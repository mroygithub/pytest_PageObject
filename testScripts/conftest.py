import sys
sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager





@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()







