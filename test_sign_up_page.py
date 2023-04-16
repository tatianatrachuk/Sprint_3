from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration():

    def test_sign_up_with_correct_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.NAME, 'name').send_keys('Татьяна')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('tatiana_trachuk_07_676@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div/div/main/div/form/button').click()
        wait = WebDriverWait(driver, 45)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_sign_up_with_incorrect_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Татьяна')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('12345')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(7)
        assert driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'
        driver.quit()