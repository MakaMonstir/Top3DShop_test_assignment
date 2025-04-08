import os
import time

import pandas as pd

from selenium import webdriver
BASE_URL = "https://store.creality.com"
SCANNERS_PATH = "/collections/scanners"
PRODUCT_TAG_SELECTOR = "a.item-img"


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
