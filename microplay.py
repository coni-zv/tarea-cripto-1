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
#datos registro
nombre="Moca"
apellido="Aoba"
email="aobamoca00@gmail.com" #este valor se puede cambiar, dado a que ya trabaje con este correo
password="Bread999"
new_pass="Bread000" 
rut="16889085-0" #obtenido de generador de rut para desarrolladores, se puede cambiar este valor generando un rut aqui: https://generarut.cl/
telefono="999999999"
region="13" # RM  de Santiago
comuna="13101" # Santiago Centro
calle="plaza 123"
n_calle="12"
fecha="03/09/1999"
pregunta="2" #cual es tu color favorito?
respuesta="azul"

def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.microplay.cl")
    return driver

def registrar():
    driver = browser()
    micuenta = driver.find_element_by_link_text('Mi cuenta')
    micuenta.click()
    time.sleep(1)
    reg = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[5]/input[2]')
    reg.click()
    time.sleep(1)
    driver.find_element_by_name("data[Clientes][name]").send_keys(nombre)
    driver.find_element_by_name("data[Clientes][apellido]").send_keys(apellido)
    driver.find_element_by_name("data[Clientes][email]").send_keys(email)
    driver.find_element_by_name("data[Clientes][email2]").send_keys(email)
    driver.find_element_by_name("data[Clientes][pass]").send_keys(password)
    driver.find_element_by_name("data[Clientes][pass2]").send_keys(password)
    driver.find_element_by_name("data[Clientes][rut]").send_keys(rut)
    driver.find_element_by_name("data[Clientes][fono]").send_keys(telefono)
    select_region = Select(driver.find_element_by_xpath('//*[@id="ClientesRegion"]'))
    select_region.select_by_value(region)
    time.sleep(1)
    select_comuna = Select(driver.find_element_by_xpath('//*[@id="ClientesComune"]'))
    select_comuna.select_by_value(comuna)
    driver.find_element_by_name("data[Clientes][address]").send_keys(calle)
    driver.find_element_by_name("data[Clientes][num]").send_keys(n_calle)
    driver.find_element_by_name("data[Clientes][birthdate]").send_keys(fecha)
    time.sleep(2)
    crearcuenta = driver.find_element_by_xpath('//*[@id="ClientesSendForm"]/div[18]/button')
    crearcuenta.click()
    time.sleep(10)

def login():
    driver = browser()
    micuenta = driver.find_element_by_link_text('Mi cuenta')
    micuenta.click()
    time.sleep(1)
    driver.find_element_by_name("data[User][email]").send_keys(email)
    driver.find_element_by_name("data[User][password]").send_keys(password)
    ingresar = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[5]/input[1]')
    ingresar.click()
    time.sleep(5)

def restablecer_pass():
    driver = browser()
    micuenta = driver.find_element_by_link_text('Mi cuenta')
    micuenta.click()
    time.sleep(1)
    forgot = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/a')
    forgot.click()
    time.sleep(5)
    entermail = driver.find_element_by_xpath('//*[@id="UserEmail"]')
    entermail.send_keys(email)
    send = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/fieldset/div[3]/input[1]')
    send.click()
    time.sleep(5)

def modificar_pass():
    driver = browser()
    micuenta = driver.find_element_by_link_text('Mi cuenta')
    micuenta.click()
    time.sleep(1)
    driver.find_element_by_name("data[User][email]").send_keys(email)
    driver.find_element_by_name("data[User][password]").send_keys(password)
    ingresar = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[5]/input[1]')
    ingresar.click()
    time.sleep(5)
    datos_pers = driver.find_element_by_link_text('Datos personales')
    datos_pers.click()
    editar = driver.find_element_by_xpath('//*[@id="tab-datos-personales"]/div/div[1]/div/ul/li[1]/a')
    editar.click()
    time.sleep(9)
    wait = WebDriverWait(driver, 300)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"fancybox-iframe")))
    datos_seg = driver.find_element_by_class_name('seguridad')
    datos_seg.click()
    time.sleep(1)
    driver.find_element_by_name("data[Clientes][pass]").send_keys(new_pass)
    driver.find_element_by_name("data[Clientes][pass2]").send_keys(new_pass)
    select_pregunta = Select(driver.find_element_by_xpath('//*[@id="tab-datos-seguridad"]/div/div/div[4]/select'))
    select_pregunta.select_by_value(pregunta) #pregunta por color favorito
    driver.find_element_by_name("data[Clientes][respuesta]").clear()
    driver.find_element_by_name("data[Clientes][respuesta]").send_keys(respuesta)
    time.sleep(2)
    guardar = driver.find_element_by_xpath('//*[@id="content_home"]/div/button[1]')
    #guardar.click() #descomentar para guardar pass modificada
    time.sleep(5)
    
def randomString(largo):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for i in range(largo))

def fuerzaBruta():
    driver = browser()
    micuenta = driver.find_element_by_link_text('Mi cuenta')
    micuenta.click()
    time.sleep(1)
    for i in range(100):
        print(i)
        driver.find_element_by_name("data[User][email]").send_keys(email)
        intento = randomString(30)
        driver.find_element_by_name("data[User][password]").send_keys(intento)
        ingresar = driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[5]/input[1]')
        ingresar.click()
        time.sleep(2)

    
#registrar()
#login()
#restablecer_pass()
#modificar_pass()
#fuerzaBruta()
