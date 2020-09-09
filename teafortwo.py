from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import string
import random

email="aobamoca00@gmail.com" #este valor se puede cambiar, dado a que ya trabaje con este correo
nombre="Moca"
apellido="Aoba"
fecha="03/09/1999"
password="Bread999"
new_pass="Bread000"

def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.tea4two.es")
    return driver

def registrar():
    driver = browser()
    reg = driver.find_element_by_xpath('//*[@id="tptn_header_links"]/ul/li[2]/a')
    reg.click()
    driver.find_element_by_xpath('//*[@id="email_create"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="uniform-customer_privacy"]/input').click()
    time.sleep(1)
    driver.find_element_by_id('SubmitCreate').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="id_gender2"]').click()
    driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys(nombre)
    driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys(apellido)
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    select_dia = Select(driver.find_element_by_xpath('//*[@id="days"]'))
    select_dia.select_by_value("3")
    select_mes = Select(driver.find_element_by_xpath('//*[@id="months"]'))
    select_mes.select_by_value("9")
    select_anio = Select(driver.find_element_by_xpath('//*[@id="years"]'))
    select_anio.select_by_value("1999")
    driver.find_element_by_xpath('//*[@id="uniform-customer_privacy"]/input').click()
    verificacion = driver.find_element_by_xpath('//*[@id="seguridad_required"]')
    texto = driver.find_element_by_xpath('//*[@id="account-creation_form"]/div[1]/div[10]/span/b').text
    verificacion.send_keys(texto)
    cookies = driver.find_element_by_xpath('//*[@id="lgcookieslaw_accept"]')
    cookies.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="submitAccount"]').click()
    time.sleep(5)

def login():
    driver = browser()
    driver.find_element_by_xpath('//*[@id="tptn_header_links"]/ul/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    cookies = driver.find_element_by_xpath('//*[@id="lgcookieslaw_accept"]')
    cookies.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="SubmitLogin"]').click()
    time.sleep(5)
    
def restablecer_pass():
    driver = browser()
    driver.find_element_by_xpath('//*[@id="tptn_header_links"]/ul/li[1]/a').click()
    time.sleep(1)
    cookies = driver.find_element_by_xpath('//*[@id="lgcookieslaw_accept"]')
    cookies.click()
    driver.find_element_by_xpath('//*[@id="login_form"]/div/p[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="form_forgotpassword"]/fieldset/p/button').click()
    time.sleep(5)

def modificar_pass():
    driver = browser()
    driver.find_element_by_xpath('//*[@id="tptn_header_links"]/ul/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    cookies = driver.find_element_by_xpath('//*[@id="lgcookieslaw_accept"]')
    cookies.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="SubmitLogin"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="center_column"]/div[2]/ul/li[5]/a/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="old_passwd"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(new_pass)
    driver.find_element_by_xpath('//*[@id="confirmation"]').send_keys(new_pass)
    driver.find_element_by_xpath('//*[@id="center_column"]/form/fieldset/div[11]/button').click()
    time.sleep(5)

def randomString(largo):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for i in range(largo))

def fuerzaBruta():
    driver = browser()
    driver.find_element_by_xpath('//*[@id="tptn_header_links"]/ul/li[1]/a').click()
    time.sleep(3)
    cookies = driver.find_element_by_xpath('//*[@id="lgcookieslaw_accept"]')
    cookies.click()
    for i in range(100):
        print(i)
        intento = randomString(30)
        driver.find_element_by_xpath('//*[@id="email"]').clear()
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(intento)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="SubmitLogin"]').click()
        time.sleep(2)
#registrar()
#login()
#restablecer_pass()
#modificar_pass()
#fuerzaBruta()
