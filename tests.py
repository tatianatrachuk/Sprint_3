from selenium import webdriver
from test_log_in_page import *
from test_sign_up_page import *
from test_section_constructor import *
from test_personal_area import *
import pytest

def web_test_start():

    driver = webdriver.Chrome()
    sigh_up = Registration(driver)
    sigh_up.test_sign_up_with_correct_password()
    sigh_up.test_sign_up_with_incorrect_password()

    log_in = Authorization(driver)
    log_in.test_log_in_by_button_login_account()
    log_in.test_log_in_by_button_personal_area()
    log_in.test_log_in_by_button_in_registraion()
    log_in.test_log_in_button_in_password_recovery()

    personal_page = Personal(driver)
    personal_page.test_go_to_personal_account()
    personal_page.test_go_to_constructor()
    personal_page.test_go_to_logo()
    personal_page.test_log_out()

    section_constructor = Constructor(driver)
    section_constructor.test_go_to_section_bulki()
    section_constructor.test_go_to_section_sauces()
    section_constructor.test_go_to_section_stuffing()


web_test_start()