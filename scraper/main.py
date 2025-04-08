import os
import time
from typing import List

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
BASE_URL = "https://store.creality.com"
SCANNERS_PATH = "/collections/scanners"
PRODUCT_TAG_SELECTOR = "a.item-img"

def find_all_elements_by_selector(
    driver: WebDriver, base_url: str, path: str, selector: str
) -> List[WebElement]:
    print(base_url + path)
    driver.get(base_url + path)
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    return elements

def main():
    driver = get_driver()
    test_call(driver=driver)
    pass


def test_call(driver):
    driver.get("https://store.creality.com/collections/scanners")
    assert "3D" in driver.title


def get_driver() -> webdriver.Remote:
    driver = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub",
        options=webdriver.ChromeOptions()
    )
    return driver


if __name__ == "__main__":
    time.sleep(5)
    main()
