from selenium import webdriver
import test_log_in_page as log_in
import test_sign_up_page as sigh_up
import test_section_constructor as section_constructor
import test_personal_area as personal_page
import pytest



@pytest.fixture
def web_test_start():

    log_in.test_log_in_by_button_login_account()
    log_in.test_log_in_by_button_personal_area()
    log_in.test_log_in_by_button_in_registraion()
    log_in.test_log_in_button_in_password_recovery()

    personal_page.test_go_to_personal_account()
    personal_page.test_go_to_constructor()
    personal_page.test_go_to_logo()
    personal_page.test_log_out()

    section_constructor.test_go_to_section_bulki()
    section_constructor.test_go_to_section_sauces()
    section_constructor.test_go_to_section_stuffing()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def registration():
    sigh_up.test_sign_up_with_correct_password()
    sigh_up.test_sign_up_with_incorrect_password()


