from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_ice_spirit():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com/')

    driver.find_element(By.CSS_SELECTOR, "[href*='/cards']").click()
    time.sleep(2)
    ice_spirit = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")

    assert ice_spirit.is_displayed()

def test_lava_hound():
    driver = webdriver.Chrome()

    driver.get('https://statsroyale.com/')

    driver.find_element(By.CSS_SELECTOR, "[href*='/cards']").click()
    time.sleep(2)
    lava_hound = driver.find_element(By.CSS_SELECTOR, "[href*='Lava+Hound']")
    assert lava_hound.is_displayed()


def test_common_cards_only():
    driver = webdriver.Chrome()

    driver.get('https://statsroyale.com/')

    driver.find_element(By.CSS_SELECTOR, "[href*='/cards']").click()
    time.sleep(2)
    ice_spirit = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    commonBox = driver.find_element(By.CSS_SELECTOR, "[name*='common-cards']")

    commonBox.click()

    assert ice_spirit.is_displayed() == False