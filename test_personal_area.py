from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class TestPersonal():

    def test_go_to_personal_account(self):

        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a')))
        element.click()
        wait = WebDriverWait(driver, 45)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_go_to_constructor(self):

        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        driver.find_element(By.CSS_SELECTOR, 'li:nth-child(1)').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_go_to_logo(self):

        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/div').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_log_out(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.NAME, 'name').send_keys('tatiana_trachuk_07_125@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('123456')
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button').click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a')))
        driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/header/nav/a').click()
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'li:nth-child(1)').click()
        driver.implicitly_wait(70)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
