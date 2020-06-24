import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PhoneCatalogTest(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome("c:/Users/TarasovaYuliya/AppData/Local/Programs/Python/Python37/chromedriver")

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def testLoginLogout(self):
        driver = self.driver
        # открытие в Chrome страницы http://127.0.0.1:8000/phones/ на которой есть кнопка Войти
        driver.get("http://127.0.0.1:8000/phones/")
        # ждем 2 секунды
        time.sleep(2)
        # поиск ссылки с текстом "Войти"
        elem = driver.find_element_by_link_text("Войти")
        # нажатие на ссылку
        elem.click()
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath (тег input с name='username')
        elem = driver.find_element_by_xpath("//input[@name='username']")
        # ввод логина
        elem.send_keys("admin")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("admin")
        # ждем 2 секунды
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)
        # проверка наличия на странице строки "Привет, admin!" после входа
        self.assertIn("Привет, admin!", driver.page_source)
        # ждем 2 секунды
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/phones/logout")
        # ждем 2 секунды
        time.sleep(2)
        # проверка отсутствия на странице строки "Привет, admin!" после выхода
        self.assertNotIn("Привет, admin!", driver.page_source)

    def testAddPhone(self):
        driver = self.driver
        # открытие в Chrome страницы http://127.0.0.1:8000/phones/ на которой есть кнопка Добавить абонента
        driver.get("http://127.0.0.1:8000/phones/")
        # ждем 2 секунды
        time.sleep(2)
        # поиск ссылки с текстом "Войти"
        elem = driver.find_element_by_link_text("Войти")
        # нажатие на ссылку
        elem.click()
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath (тег input с name='username')
        elem = driver.find_element_by_xpath("//input[@name='username']")
        # ввод логина
        elem.send_keys("admin")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("admin")
        # ждем 2 секунды
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)
        # поиск ссылки с текстом "Добавить абонента"
        elem = driver.find_element_by_link_text("Добавить абонента")
        # нажатие на ссылку
        elem.click()
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath (тег input с name='fio')
        elem = driver.find_element_by_xpath("//input[@name='fio']")
        elem.send_keys("Test")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='address')
        elem = driver.find_element_by_xpath("//input[@name='address']")
        elem.send_keys("Address Test")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='phone1')
        elem = driver.find_element_by_xpath("//input[@name='phone1']")
        elem.send_keys("+372001112233")
        # ждем 2 секунды
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)

    def testNewUser(self):
        driver = self.driver
        # открытие в Chrome страницы http://127.0.0.1:8000/phones/ на которой есть кнопка Зарегистрироваться
        driver.get("http://127.0.0.1:8000/phones/")
        # ждем 2 секунды
        time.sleep(2)
        # поиск ссылки с текстом "Зарегистрироваться"
        elem = driver.find_element_by_link_text("Зарегистрироваться")
        # нажатие на ссылку
        elem.click()
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath (тег input с name='username')
        elem = driver.find_element_by_xpath("//input[@name='username']")
        # ввод логина
        elem.send_keys("TestUser")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='password1')
        elem = driver.find_element_by_xpath("//input[@name='password1']")
        # ввод логина
        elem.send_keys("qweGH1642")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='password2')
        elem = driver.find_element_by_xpath("//input[@name='password2']")
        # ввод логина
        elem.send_keys("qweGH1642")
        # ждем 2 секунды
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода логина по XPath (тег input с name='username')
        elem = driver.find_element_by_xpath("//input[@name='username']")
        # ввод логина
        elem.send_keys("TestUser")
        # ждем 2 секунды
        time.sleep(2)
        # поиск текстового поля для ввода пароля по XPath (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("qweGH1642")
        # ждем 2 секунды
        time.sleep(2)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
