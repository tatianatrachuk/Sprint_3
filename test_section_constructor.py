from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor():

    def test_go_to_section_bulki(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]').click()
        WebDriverWait(driver, 9)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'
        driver.quit()

    def test_go_to_section_sauces(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[3]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa74'
        driver.quit()

    def test_go_to_section_stuffing(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.find_element(By.XPATH, '/html/body/div[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'
        driver.quit()