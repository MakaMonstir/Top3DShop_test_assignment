import os
import time
from typing import Dict, List

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

load_dotenv(dotenv_path=".env")

REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL")
BASE_URL = "https://store.creality.com"
SCANNERS_PATH = "/collections/scanners"
SELECTOR = By.CSS_SELECTOR
PRODUCT_TAG_SELECTOR = "a.item-img"
PROUDCT_NAME_SELECTOR = "div.product-main > h1"
PROUDCT_PRICE_SELECTOR = "div.product-price span.price"
PROUDCT_SHIPPING_DATE_SELECTOR = "div.product-info " \
                                 "div.product-info-item-content > span"


def get_driver() -> WebDriver:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=800x600")

        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.fonts": 2,
            "profile.managed_default_content_settings.stylesheets": 1,
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Remote(command_executor=REMOTE_URL, options=options)
        return driver
    except Exception as e:
        print(f"Failed to setup driver: {e}")
        raise


def find_all_elements_by_selector(
    driver: WebDriver, path: str, selector: str
) -> List[WebElement]:
    driver.get(BASE_URL + path)
    elements = driver.find_elements(SELECTOR, selector)
    return elements


def get_links_from_elements(elements: List[WebElement]) -> List[str]:
    links = [
        elem.get_attribute("href")
        for elem in elements
        if elem.get_attribute("href") is not None
    ]
    return links


def parse_item_page(
        driver: WebDriver, path: str, selectors: Dict[str, str]
) -> Dict[str, str]:

    driver.get(BASE_URL + path)

    records = {}
    for key, selector in selectors.items():
        try:
            element = driver.find_element(SELECTOR, selector)
            text = element.text

        except NoSuchElementException:
            print(f'No element found by given selector "{selector}" '
                  f'on path "{path}". Skipping.')
            text = None

        records[key] = text

    return records


def main():
    driver = get_driver()

    web_elements = find_all_elements_by_selector(
        driver=driver,
        path=SCANNERS_PATH,
        selector=PRODUCT_TAG_SELECTOR,
    )

    links = get_links_from_elements(web_elements)

    selectors = {
        'name': PROUDCT_NAME_SELECTOR,
        'price': PROUDCT_PRICE_SELECTOR,
        'shipping_date': PROUDCT_SHIPPING_DATE_SELECTOR,
    }
    for link in links:
        data = parse_item_page(driver, SCANNERS_PATH, selectors)
        print(data)


if __name__ == "__main__":
    time.sleep(float(os.getenv("TIME_TO_SLEEP")))  # wait until Selenium Standalone started
    main()
