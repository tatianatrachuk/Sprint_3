from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class TestAuthorization():

    def test_log_in_by_button_login_account(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//button").click()
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(70)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', driver.quit()
        driver.quit()

    def test_log_in_by_button_personal_area(self):

        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        wait = WebDriverWait(driver, 45)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', driver.quit()
        driver.quit()

    def test_log_in_by_button_in_registraion(self):

        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/div/p/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(5)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', driver.quit()
        driver.quit()

    def test_log_in_button_in_password_recovery(self):

        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p[2]/a').click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p/a').click()
        driver.implicitly_wait(3)
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(50)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', driver.quit()
        driver.quit()