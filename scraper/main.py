import os

import pandas as pd

from selenium import webdriver

driver = webdriver.Remote(
    command_executor="http://chrome:4444/wd/hub",
    options=webdriver.ChromiumOptions()
)


def main():
    pass


if __name__ == "__main__":
    main()
