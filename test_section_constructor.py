from selenium.webdriver.common.by import By
from time import sleep

class Constructor():

    def __init__(self, driver):
        self.driver = driver

    def test_go_to_section_bulki(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'
        self.driver.quit()

    def test_go_to_section_sauces(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[3]').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa74'
        self.driver.quit()

    def test_go_to_section_stuffing(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        self.driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_124@ya.ru')
        self.driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        self.driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]').click()
        sleep(3)
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'
        self.driver.quit()