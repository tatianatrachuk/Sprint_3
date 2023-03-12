from selenium.webdriver.common.by import By
from time import sleep

class Registration():

    def __init__(self, driver):
        self.driver = driver

    def test_sign_up_with_correct_password(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Татьяна')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(5)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        self.driver.quit()

    def test_sign_up_with_incorrect_password(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Татьяна')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('12345')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        assert self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'
        self.driver.quit()