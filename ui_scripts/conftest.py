import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    print("Starting webdriver")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("Terminating browser")