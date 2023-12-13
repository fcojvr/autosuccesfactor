
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Functions.Funciones2 import Funciones_Globales
from Functions.Funciones_Ex import Funexcel

service = Service("C:/Chromedriver/chromedriver.exe")

@pytest.fixture(scope='module')
def setup_login_QA():
    global driver, f , fe
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales(driver)
    fe = Funexcel(driver)
    f.configure_logging() 
    link_page, user, password, id_empleado, f_ingreso, sociedad  = fe.get_test_data()
    f.Navegar(link_page, 1)
    f.text_val("xpath", "//input[contains(@id,'input1-inner')][@name='username']", user, .4)
    f.text_val("xpath", "//input[contains(@id,'input2-inner')][@name='password']", password, .4)
    f.click_val("xpath", "//span[contains(@id,'button2-inner')][@class='sapMBtnInner sapMBtnHoverable sapMFocusable sapMBtnText sapMBtnEmphasized'][contains(.,'Iniciar sesión')]", 4)
    print("Entrando al sistema...")
    yield driver, f, id_empleado, f_ingreso, sociedad
    driver.quit() 
    

@pytest.fixture(scope='module')
def setup_login_dev():
    global driver, f , fe
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales(driver)
    fe = Funexcel(driver)
    link_page, user, password, id_empleado = fe.get_test_data()
    f.Navegar(link_page, 1)
    driver.implicitly_wait(15)
    f.text_val("xpath", "//input[contains(@id,'input1-inner')][@name='username']", user, .4)
    f.text_val("xpath", "//input[contains(@id,'input2-inner')][@name='password']", password, .4)
    f.click_val("xpath", "//span[contains(@id,'button2-inner')][@class='sapMBtnInner sapMBtnHoverable sapMFocusable sapMBtnText sapMBtnEmphasized'][contains(.,'Iniciar sesión')]", 4)
    print("Entrando al sistema...")
    yield id_empleado