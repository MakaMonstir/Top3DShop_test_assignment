import os

import pandas as pd

from selenium import webdriver

driver = webdriver.Remote(
    command_executor="http://chrome:4444/wd/hub",
    options=webdriver.ChromeOptions()
)


def main():
    test_call()
    pass


def test_call(driver):
    driver.get("https://store.creality.com/collections/scanners")
    assert "3D" in driver.title


if __name__ == "__main__":
    main()
