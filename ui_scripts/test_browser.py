import time

from selenium import webdriver


def test_google(browser):
    browser.get("https://google.com")
    time.sleep(5)

def test_apple(browser):
    browser.get("https://apple.com")
    time.sleep(5)