from selenium.webdriver.common.by import By
from time import sleep

class Personal():

    def __init__(self, driver):
        self.driver = driver

    def test_go_to_personal_account(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        self.driver.quit()

    def test_go_to_constructor(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/ul/li[1]/a').click()
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()

    def test_go_to_logo(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/div').click()
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        self.driver.quit()

    def test_log_out(self):

        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        sleep(3)
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/nav/ul/li[3]/button').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        self.driver.quit()