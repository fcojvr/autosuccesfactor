import pytest
import time
import os
import sys
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import logging
from selenium.common.exceptions import StaleElementReferenceException
from behave import given, when, then
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "Funciones2"))
sys.path.append("C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/Autosuccessfactor/Functions/Funciones2")
from Functions.Funciones2 import Funciones_Globales
from Functions.Funciones_Ex import Funexcel
from setup.Setup import setup_login_QA

service = Service("C:/Chromedriver/chromedriver.exe")
logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup_login_QA")
def test_altaEmployee(setup_login_QA):
    driver, f, id_empleado, f_ingreso, sociedad = setup_login_QA
    f.click_val("xpath","//div[@class='LineClampText_lineClamp__1hlRY ActionChip_quickActionLabel__1VkVx LineClampText_multiline__2pJux'][contains(.,'Ver Organigrama')]", 5)
    f.click_val("xpath", "//span[contains(@id,'xmlview0--newHireButton-img')][@data-sap-ui='__xmlview0--newHireButton-img']", 2)
    wait = WebDriverWait(driver, 10)
    hiredate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-roledescription='Entrada de fecha']")))
    try:
        hiredate.clear()
        hiredate.send_keys(str(f_ingreso) + Keys.TAB + str(sociedad))
        print("Escribiendo en el campo el texto:", f_ingreso)
    except StaleElementReferenceException:
        print("La referencia del elemento es obsoleta. Volviendo a intentar...")
        # Reintentar localizar el elemento y realizar la acción
        hiredate = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-roledescription='Entrada de fecha']")))
        hiredate.clear()
        hiredate.send_keys(str(f_ingreso) + Keys.TAB + str(sociedad))
        print("Escribiendo en el campo el texto:", f_ingreso)
        time.sleep(2)
        f.click_val("xpath", "//li[contains(@role,'option')]", 2)
        f.click_val("xpath", "//span[contains(@data-sap-ui,'__box1-arrow')]", 2)
        f.click_val("xpath", "(//li[contains(@aria-setsize,'2')])[1]", 2)
        f.click_val("xpath", "(//span[contains(@aria-label,'Opciones de selección')])[3]", 3)
        f.click_val("xpath", "//li[contains(.,'Plantilla estándar')]", 3)
        f.click_val("xpath","(//span[contains(.,'Continuar')])[2]", 2)
        