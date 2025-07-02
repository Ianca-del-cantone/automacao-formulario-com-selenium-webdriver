import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


class PreencherFormulario:
    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        time.sleep(1)

    def inserir_nome(self, nome):
        self.driver.find_element(By.ID, "name").send_keys(nome)
        time.sleep(1)

    def inserir_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def escolher_genero(self):
        self.driver.find_element(By.XPATH, '(//input[@type="radio"])[2]').click()

    def inserir_numero(self, numero):
        self.driver.find_element(By.ID, "mobile").send_keys(numero)
        time.sleep(1)

    def inserir_data_aniversario(self, data):
        self.driver.find_element(By.ID, "dob").send_keys(data)
        time.sleep(1)

    def inserir_assunto(self, assunto):
        self.driver.find_element(By.ID, "subjects").send_keys(assunto)
        time.sleep(1)

    def escolher_hobbies(self):
        self.driver.find_element(By.XPATH, '(//input[@type="checkbox"])[3]').click()
        time.sleep(1)

    def escolher_arquivo(self):
        self.driver.find_element(By.ID, "picture").send_keys(r"C:\Users\Ianca Honorato\Downloads\SeleniumWebdriver.png")
        time.sleep(1)

    def endereco_atual(self, endereco):
        self.driver.find_element(By.CSS_SELECTOR, "textarea#picture").send_keys(endereco)
        time.sleep(2)

    def escolher_estado(self):
        select_element = self.driver.find_element(By.ID, "state")
        select = Select(select_element)
        select.select_by_value("Haryana")
        time.sleep(1)

    def escolher_cidade(self):
        select_element = self.driver.find_element(By.ID, "city")
        select = Select(select_element)
        select.select_by_index(1)
        time.sleep(1)

    def clicar_login(self):
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        time.sleep(1)


formulario = PreencherFormulario(driver)

formulario.abrir_pagina()
formulario.inserir_nome("Ianca Del Cantone")
formulario.inserir_email("iancadch@gmail.com")
formulario.escolher_genero()
formulario.inserir_numero('31 9991-2332')
formulario.inserir_data_aniversario('23/02/1997')
formulario.inserir_assunto("Computer Science")
formulario.escolher_hobbies()
formulario.escolher_arquivo()
formulario.endereco_atual("Rua das Flores, nº 123 - Centro, Belo Horizonte - MG")
formulario.escolher_estado()
formulario.escolher_cidade()
formulario.clicar_login()


driver.quit()























