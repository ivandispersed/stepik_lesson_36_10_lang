import pytest
from selenium.webdriver.common.by import By
import time

#Основной тест задания
def test_if_addbasket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    #Добавляю ожидание перед тестовой проверкой, чтобы можно было визуально осмотреть открытый сайт
    #Я выставил 10 вместо 30 секунд, чтобы не тратить лишнее время рецензентов; если этого мало, то поменяйте время ожидания на удобное вам
    
    time.sleep(10)
    
    #Если кнопка есть, то вернётся список (т.е. не False), assert выполнится и тест пройдёт; 
    #если кнопки нет, то вернётся пустой список, в булевой логике python это False, assert провалится вместе с тестом    
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "There is no add-basket button!"

