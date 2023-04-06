import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_accept_basket_available(browser):
    browser.get(link)
    time.sleep(30)
    x = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(x) > 0, 'basket is not available'