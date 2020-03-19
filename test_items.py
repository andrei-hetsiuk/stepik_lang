import pytest
from selenium import webdriver



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.get(link)
    browser.implicitly_wait(3)
    b = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]').size != 0
    assert b , "Кнопка добавления товара отсутствует"
