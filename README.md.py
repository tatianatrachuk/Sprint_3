# Проект автоматизации тестирования сервиса Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest.
2. Установить selenium — pip install selenium.
3. Запуск тестов — из  директории с помощью команды pytest -v -s .

Описание локаторов:
driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') #Поле ввода имени
driver.find_element(By.NAME, 'name') #Поле ввода почты
driver.find_element(By.NAME, 'Пароль') #Поле ввода пароля
driver.find_element(By.XPATH, 'html/body/div[@id="root"]/div/main/div/form/button') #Кнопка войти