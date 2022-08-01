# import time
from selenium.webdriver.common.by import By


# pytest --tb=line --language=es test_items.py
def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(5)
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert len(buttons) == 1, 'Add to basket button is not visible'
