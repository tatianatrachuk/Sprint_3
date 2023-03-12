from selenium.webdriver.common.by import By
from time import sleep

class Authorization():

    def __init__(self, driver):
        self.driver = driver

    def test_log_in_by_button_login_account(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()

    def test_log_in_by_button_personal_area(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()

    def test_log_in_by_button_in_registraion(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/register')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/div/p/a').click()
        sleep(3)
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()

    def test_log_in_button_in_password_recovery(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p[2]/a').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p/a').click()
        sleep(3)
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()