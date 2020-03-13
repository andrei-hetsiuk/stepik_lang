#import pandas as pd

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
# df = pd.read_csv(r'C:\Users\ah\Desktop\testpy\4.csv', sep=';', encoding ='cp1252' )
# df = pd.DataFrame(df,columns=['id','field','field1','field3','name','surname','field4','field5','field6','field7','field8','field9','field10','field11','tel','code','number'])
# df['new'] = df['code'] +' '+ df['number']
# df.to_csv(r'C:\Users\ah\Desktop\testpy\concat.csv')

#--------------------------------------------------------------
#import os

# define the name of the directory to be created
#for i in range(4,27):
#	os.mkdir(r'C:/Users/ah/Desktop/rew/' + '2019-AC-cleansing-cross' + str(i))
# from selenium import webdriver
# import time 
# import math

# link = "http://suninjuly.github.io/find_link_text"



# try:
    # browser = webdriver.Chrome()
    # browser.get(link)
    # link = browser.find_element_by_partial_link_text("224")
    # link.click()
    # input1 = browser.find_element_by_tag_name("input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name("last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_class_name("form-control.city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

# finally:
    # # успеваем скопировать код за 30 секунд
    # time.sleep(30)
    # # закрываем браузер после всех манипуляций
    # browser.quit()

# # не забываем оставить пустую строку в конце файла
#--------------------------------------------------------------
#import time
#link = "http://suninjuly.github.io/find_xpath_form"
#try:
#     browser = webdriver.Chrome()
#     browser.get(link)
	
#     button = browser.find_element_by_xpath("//input[@name='first_name']")
#     button.send_keys("Ivan")
#     button = browser.find_element_by_xpath("//input[@name='last_name']")
#     button.send_keys("Ivan")
#     button = browser.find_element_by_xpath("//input[@class='form-control city']")
#     button.send_keys("Ivan")
#     button = browser.find_element_by_xpath("//input[@id='country']")
#     button.send_keys("Ivan")
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#------------------------------------------------------------
# from selenium import webdriver
# import time
# import math

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try: 
    # link = "http://suninjuly.github.io/math.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_id('input_value')
    # x = x_element.text
    # y = calc(x)
    # x_element = browser.find_element_by_id('answer')
    # x_element.send_keys(y)
    # checkbutton = browser.find_element_by_id('robotCheckbox')
    # checkbutton.click()
    # radbutton = browser.find_element_by_id('robotsRule')
    # radbutton.click()
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # browser.quit()
	
#-------------------------------------------------------------------
# from selenium import webdriver
# import time
# import math

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try: 
    # link = "http://suninjuly.github.io/get_attribute.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_id('treasure')
    # x = x_element.get_attribute("valuex")
    # y = calc(x)
    # print(y)
    # x_element = browser.find_element_by_id('answer')
    # x_element.send_keys(y)
    # checkbutton = browser.find_element_by_id('robotCheckbox')
    # checkbutton.click()
    # radbutton = browser.find_element_by_id('robotsRule')
    # radbutton.click()
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # browser.quit()
	#---------------------------------------------------------
# from selenium import webdriver
# import time
# import math
# from selenium.webdriver.support.ui import Select


# try: 
    # link = "http://suninjuly.github.io/selects1.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # element1 = browser.find_element_by_id('num1')
    # x = element1.text
    # element2 = browser.find_element_by_id('num2')
    # y = element2.text
    # x = str(int(x) + int(y))
	
    # select = Select(browser.find_element_by_id("dropdown"))
    # select.select_by_value(x)
	
    
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(5)
    # # закрываем браузер после всех манипуляций
    # browser.quit()
#------------------------------------------------------------

# from selenium import webdriver
# import time
# import math

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try: 
    # link = "http://suninjuly.github.io/execute_script.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_id('input_value')
    # x = x_element.text
    # y = calc(x)
    # browser.execute_script("window.scrollBy(0, 100);")
    # x_element = browser.find_element_by_id('answer')
    # x_element.send_keys(y)
    # checkbutton = browser.find_element_by_id('robotCheckbox')
    # checkbutton.click()
    # radbutton = browser.find_element_by_id('robotsRule')
    # radbutton.click()
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # # browser.quit()
#-----------------------------2.2.1------------------------------------------------

# from selenium import webdriver
# import time
# import math
# import os 

# try: 
    # link = "http://suninjuly.github.io/file_input.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_name('firstname')
    # x_element.send_keys("asasa")
    # x_element = browser.find_element_by_name('lastname')
    # x_element.send_keys("asasa")
    # x_element = browser.find_element_by_name('email')
    # x_element.send_keys("asasa")
    # current_dir = os.path.abspath(os.path.dirname(""))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, '2.py')
    # x_element = browser.find_element_by_id('file')
    # x_element.send_keys(file_path)
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(3)
    # # закрываем браузер после всех манипуляций
    # browser.quit()	
	
#---------------------------------2.3.2-----------------------------------------------
# from selenium import webdriver
# import time
# import math

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try: 
    # link = "http://suninjuly.github.io/alert_accept.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_xpath("//button[contains(@type,'submit')]")
    # x_element.click()
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # x_element = browser.find_element_by_id("input_value")
    # x = x_element.text
    # y = calc(x)
    # x_element = browser.find_element_by_id('answer')
    # x_element.send_keys(y)
    
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # browser.quit()
	
#------------------------------------2.3.3---------------------------------------------
# from selenium import webdriver
# import time
# import math

# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try: 
    # link = "http://suninjuly.github.io/redirect_accept.html"
    # browser = webdriver.Chrome()
    # browser.get(link)
    # print(type(browser))
    # # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_class_name('trollface')
    # print(type(x_element))
    # x_element.click()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    # x_element = browser.find_element_by_id("input_value")
    # x = x_element.text
    # y = calc(x)
    # x_element = browser.find_element_by_id('answer')
    # x_element.send_keys(y)
    
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(10)

    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # browser.quit()
	
#---------------------------------------------testMSCRM-----------------------------------------------
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# try:
    # browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)
    # browser.get("http://mscrm:5555/AdventureWorksCycle/main.aspx#974395334")
    # iframe = browser.find_element_by_xpath("//iframe[@id='InlineDialog_Iframe']")
    # browser.switch_to.frame(iframe)
    # button = browser.find_element_by_xpath("//div[@id='navTourCloseButtonImage']")
    # button.click()
    # browser.switch_to.default_content()
    # button = browser.find_element_by_class_name('navTabButtonArrowDown')
    # button.click()
    # button = browser.find_element_by_xpath('//span[contains(text(), "Accounts")]')
    # button.click()
    # button = browser.find_element_by_xpath('//span[contains(text(), "New")]')
    # button.click()
    # browser.refresh()
    # button = browser.find_element_by_xpath('//span[contains(text(), "New")]')
    # button.click()
    
    # button = WebDriverWait(browser, 5).until(
        # EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "New")]'))
    # )
    # button.click()
    
    
	
# finally:
    # time.sleep(5)
    # browser.quit()
#----------------------------------------2.4.8--------------------------------------------------
# from selenium import webdriver
# import time
# import math
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# def calc(x):
	# return str(math.log(abs(12*math.sin(int(x)))))
# try:
    # browser = webdriver.Chrome()
    # # говорим WebDriver искать каждый элемент в течение 5 секунд
    
    # browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # button = WebDriverWait(browser, 12).until(
        # EC.text_to_be_present_in_element((By.ID, 'price'), str('$100'))
    # )
    # button = browser.find_element_by_id("book").click()
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # x = browser.find_element_by_id("input_value").text
    # y = calc(x)
    # button = browser.find_element_by_id("answer")
    # button.send_keys(y)
    # button = browser.find_element_by_id("solve").click()
    
    
	
# finally:
    # time.sleep(5)
    # #browser.quit()
	
#---------------------------------------------------3.2.1------------------------------------------
# def test_input_text(expected_result, actual_result):
    # assert str(expected_result) == str(actual_result), f"expected {expected_result}, got {actual_result}"
#--------------------------------------------------3.2.12------------------------------------------
# import unittest
# from selenium import webdriver
# import time

# class TestAbs(unittest.TestCase):
    # def test_abs1(self):
        # try: 
            # link = "http://suninjuly.github.io/registration1.html"
            # browser = webdriver.Chrome()
            # browser.get(link)

            # # Ваш код, который заполняет обязательные поля
            # browser = webdriver.Chrome()
            # browser.get(link)
            # button = browser.find_element_by_xpath("//input[contains(@placeholder,'first')]")
            # button.send_keys("adsdf")
            # button = browser.find_element_by_xpath("//input[contains(@placeholder,'last')]")
            # button.send_keys("adsdf")
            # button = browser.find_element_by_xpath("//input[contains(@class,'third')]")
            # button.send_keys('sdfsfsf')

            # # Отправляем заполненную форму
            # button = browser.find_element_by_css_selector("button.btn")
            # button.click()

            # # Проверяем, что смогли зарегистрироваться
            # # ждем загрузки страницы
            # time.sleep(1)

            # # находим элемент, содержащий текст
            # welcome_text_elt = browser.find_element_by_tag_name("h1")
            # # записываем в переменную welcome_text текст из элемента welcome_text_elt
            # welcome_text = welcome_text_elt.text

            # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # self.assertEqual(welcome_text,"Congratulations! You have successfully registered!" , "Should be absolute value of a number")
            

        # finally:
            # # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # # закрываем браузер после всех манипуляций
            # browser.quit()
    # def test_abs2(self):
        # try: 
            # link = "http://suninjuly.github.io/registration2.html"
            # browser = webdriver.Chrome()
            # browser.get(link)

            # # Ваш код, который заполняет обязательные поля
            # browser = webdriver.Chrome()
            # browser.get(link)
            # button = browser.find_element_by_xpath("//input[contains(@placeholder,'first')]")
            # button.send_keys("adsdf")
            # button = browser.find_element_by_xpath("//input[contains(@placeholder,'last')]")
            # button.send_keys("adsdf")
            # button = browser.find_element_by_xpath("//input[contains(@class,'third')]")
            # button.send_keys('sdfsfsf')

            # # Отправляем заполненную форму
            # button = browser.find_element_by_css_selector("button.btn")
            # button.click()

            # # Проверяем, что смогли зарегистрироваться
            # # ждем загрузки страницы
            # time.sleep(1)

            # # находим элемент, содержащий текст
            # welcome_text_elt = browser.find_element_by_tag_name("h1")
            # # записываем в переменную welcome_text текст из элемента welcome_text_elt
            # welcome_text = welcome_text_elt.text

            # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # self.assertEqual(welcome_text,"Congratulations! You have successfully registered!" , "Should be absolute value of a number")
            

        # finally:
            # # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # # закрываем браузер после всех манипуляций
            # browser.quit()
# if __name__ == "__main__":
    # unittest.main()
#----------------------------------------3.3.8------------------------------------------
# def test_abs1():
    # assert abs(-42) == 42, "Should be absolute value of a number"

# def test_abs2():
    # assert abs(-42) == -42, "Should be absolute value of a number"
#----------------------------------------3.4.2---------------------------
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1():

    # @classmethod
    # def setup_class(self):
        # print("\nstart browser for test suite..")
        # self.browser = webdriver.Chrome()

    # @classmethod
    # def teardown_class(self):
        # print("quit browser for test suite..")
        # self.browser.quit()

    # def test_guest_should_see_login_link(self):
        # self.browser.get(link)
        # self.browser.find_element_by_css_selector("#login_link")

    # def test_guest_should_see_basket_link_on_the_main_page(self):
        # self.browser.get(link)
        # self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# class TestMainPage2():

    # def setup_method(self):
        # print("start browser for test..")
        # self.browser = webdriver.Chrome()

    # def teardown_method(self):
        # print("quit browser for test..")
        # self.browser.quit()

    # def test_guest_should_see_login_link(self):
        # self.browser.get(link)
        # self.browser.find_element_by_css_selector("#login_link")

    # def test_guest_should_see_basket_link_on_the_main_page(self):
        # self.browser.get(link)
        # self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        
#-----------------------------------------------------3.5.2---------------------------------------
# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"

# @pytest.fixture(scope="function")
# def browser():
    # print("\nstart browser for test..")
    # browser = webdriver.Chrome()
    # yield browser
    # print("\nquit browser..")
    # browser.quit()


# class TestMainPage1():

    # @pytest.mark.skip
    # def test_guest_should_see_login_link(self, browser):
        # browser.get(link)
        # browser.find_element_by_css_selector("#login_link")

    # def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        # browser.get(link)
        # browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#----------------------------------3.5.6------------------------------------
# import pytest

# @pytest.mark.xfail(raises=RuntimeError)
# def test_succeed():
    # assert True


# @pytest.mark.xfail
# def test_not_succeed():
    # assert False


# @pytest.mark.skip
# def test_skipped():
    # assert False
#------------------------------------------------3.5.7------------------------------
# import pytest


# class TestMainPage():
    # # номер 1
    # @pytest.mark.xfail
    # @pytest.mark.smoke
    # def test_guest_can_login(self, browser):
        # assert True

    # # номер 2
    # @pytest.mark.regression
    # def test_guest_can_add_book_from_catalog_to_basket(self):
        # assert True


# class TestBasket():
    # # номер 3
    # @pytest.mark.skip(reason="not implemented yet")
    # @pytest.mark.smoke
    # def test_guest_can_go_to_payment_page(self):
        # assert True

    # # номер 4
    # @pytest.mark.smoke
    # def test_guest_can_see_total_price(self):
        # assert True


# @pytest.mark.skip
# class TestBookPage():
    # # номер 5
    # @pytest.mark.smoke
    # def test_guest_can_add_book_to_basket(self):
        # assert True

    # # номер 6
    # @pytest.mark.regression
    # def test_guest_can_see_book_price(self):
        # assert True


# # номер 7
# @pytest.mark.beta_users
# @pytest.mark.smoke
# def test_guest_can_open_gadget_catalogue(self):
    # assert True
#-----------------------------------3.6.3--------------------------------------
# import pytest
# from selenium import webdriver
# import time
# import math

# @pytest.fixture(scope="function")
# def browser():
    # print("\nstart browser for test..")
    # browser = webdriver.Chrome()
    # yield browser
    # print(type(browser))
    # browser.quit()

# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
# def test_guest_should_see_login_link(browser, link):
    # answer = str(math.log(int(time.time())))
    # link = f"{link}"
    # browser.get(link)
    # print(type(browser))
    # browser.implicitly_wait(10)
    # b = browser.find_element_by_xpath('//textarea[@class ="textarea string-quiz__textarea ember-text-area ember-view"]')
    # b.click()
    # b.send_keys(answer)
    # b = browser.find_element_by_xpath('//button[@class ="submit-submission"]')
    # b.click()
    # b = browser.find_element_by_xpath('//pre[@class ="smart-hints__hint"]').text
    # assert "Correct!" == b
#-----------------------------------3.6.4-----------------------------------------------------  

# import pytest
# from selenium import webdriver
# import time
# import math


# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1"])
# def test_guest_should_see_login_link(browser, link):
    # answer = str(math.log(int(time.time())))
    # link = f"{link}"
    # browser.get(link)
    # print(type(browser))
    # browser.implicitly_wait(10)
    # b = browser.find_element_by_xpath('//textarea[@class ="textarea string-quiz__textarea ember-text-area ember-view"]')
    # b.click()
    # b.send_keys(answer)
    # b = browser.find_element_by_xpath('//button[@class ="submit-submission"]')
    # b.click()
    # b = browser.find_element_by_xpath('//pre[@class ="smart-hints__hint"]').text
    # assert "Correct!" == b
    
#---------------------------------------3.6.5------------------------------------
# from selenium import webdriver

# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Firefox()

# driver.get("https://stepik.org/lesson/25969/step/8")
#------------------------------3.6.5.2--------------------------------------
# import pytest
# from selenium import webdriver
# import time
# import math


# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1"])
# def test_guest_should_see_login_link(browser, link):
    # answer = str(math.log(int(time.time())))
    # link = f"{link}"
    # browser.get(link)
    # print(type(browser))
    # browser.implicitly_wait(10)
    # b = browser.find_element_by_xpath('//textarea[@class ="textarea string-quiz__textarea ember-text-area ember-view"]')
    # b.click()
    # b.send_keys(answer)
    # b = browser.find_element_by_xpath('//button[@class ="submit-submission"]')
    # b.click()
    # b = browser.find_element_by_xpath('//pre[@class ="smart-hints__hint"]').text
    # assert "Correct!" == b
#---------------------------3.6.7---------------------------------------
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")