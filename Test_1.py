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
def test_consultaEmployee(setup_login_QA):
    driver, f, id_empleado = setup_login_QA
    f.configure_logging(logger_name=__name__)
    logging.getLogger(__name__).setLevel(logging.INFO)
    print(f"Configuración de registro: {logging.getLogger(__name__).getEffectiveLevel()}")
    try:
        driver.implicitly_wait(15)
        f.click_val("xpath","//a[contains(@aria-label,'Ver Mi perfil')]", 2)
        f.click_val("xpath", "//div[contains(@id,'picker2-fullName')][@class='fullName'][contains(.,'BRUNO EMILIO DI GAETANO')]", 2)
        f.text_val("xpath", "//input[contains(@id,'picker2--PopupFrag--searchInput-I')][@type='search']", id_empleado, 2)
        if f.Existe("//div[contains(@class,'surjUSIFullName')]", 1) == "Existe":
            f.click_val("xpath", "(//div[contains(@class,'surjUSIFullName')])[1]", 2)
            f.click_val("xpath", "(//span[contains(.,'Información de Empleo')])[4]", 2)
            f.click_val("xpath","//button[contains(@title, 'Historial de Información del puesto')]/span[contains(@class, 'sapMBtnInner')]/span[contains(@class, 'sapUiIcon')]", 2)
            last_modified = driver.find_element(By.XPATH, "(//span[contains(@class,'sapMText sapUiSelectable sapMTextMaxWidth')])[1]").text
            f.logger.info(f"El empleado se encuentra activo {last_modified}")
            time.sleep(2)
            print("El empleado se encuentra activo " + last_modified)
            event_reason = driver.find_element(By.XPATH, "(//span[@class='valuePattern'])[2]").text
            f.logger.info(f"Event Reason: {event_reason}")
            print(event_reason)
            f_effective = driver.find_element(By.XPATH, "(//span[@class='sapExtentUilibEffectiveDateText'])[1]").text
            f.logger.info(f"Effective Date: {f_effective}")
            print(f_effective)
            position = driver.find_element(By.XPATH, "(//span[@class='valuePattern'])[4]").text
            print(position)
            driver.quit()
        elif f.Existe("(//div[contains(.,'Sin datos')])[6]", 1) == "Existe":
            print("No hay empleados activos con ese ID")
            f.check_xpath("//div[@id='__box0-CbBg']",2)
            f.click_val("xpath", "(//div[contains(@class,'surjUSIFullName')])[1]", 2)
            f.click_val("xpath", "(//span[contains(.,'Información de Empleo')])[4]", 2)
            f.click_val("xpath","//button[contains(@title, 'Historial de Información del puesto')]/span[contains(@class, 'sapMBtnInner')]/span[contains(@class, 'sapUiIcon')]", 1)
            time.sleep(2)
            last_modified = driver.find_element(By.XPATH, "(//span[contains(@class,'sapMText sapUiSelectable sapMTextMaxWidth')])[1]").text
            f.logger.info(f"El empleado se encuentra inactivo {last_modified}")
            #print("El empleado se encuentra inactivo " + last_modified)
            event_reason = driver.find_element(By.XPATH, "(//span[@class='valuePattern'])[2]").text
            f.logger.info(f"Event Reason: {event_reason}")
            #print(event_reason)
            f_effective = driver.find_element(By.XPATH, "(//span[@class='sapExtentUilibEffectiveDateText'])[1]").text
            f.logger.info(f"Effective Date: {f_effective}")
            #print(f_effective)
            position = driver.find_element(By.XPATH, "(//span[@class='valuePattern'])[4]").text
            f.logger.info(f"Position: {position}")
            #print(position)
            driver.quit()
        else:
            f.logger.info("El id proporcionado es incorrecto")
            print("El id proporcionado es incorrecto")

    except NoSuchElementException as ex:
        f.logger.error(f"Error: {ex}")
        pytest.fail(f"Excepción: {ex}")

    finally:
        driver.quit()  

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
        f.click_val("xpath", "//li[@role='option'][1]", 2)

        
        

        






"""@pytest.mark.usefixtures("setup_login_QA")
def test_consultaDev():
    print("Entro al sistema dos")
    f.click_val("xpath","//a[@href='/web/index.php/admin/viewAdminModule']",2)
    f.click_val("xpath","//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]",2)
    f.click_val("xpath","(//li[contains(.,'Users')])[2]",3)
    #f.text_val("xpath","//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input","Cheeku",2)
    #f.click_val("xpath","//button[@type='submit'][contains(.,'Search')]",2)

    f.click_val("xpath","//ui5-static-area-item-sf-header[contains(@class,'ui5wc_19 sapUiSizeCompact ui5-content-density-compact')]",2)
    f.click_val("xpath","//span[contains(@data-sap-ui,'__button90-img')]",1)
    Fecha_Integración = f.SX("//span[contains(@id,'__text291')]").text
    print(Fecha_Integración)
    print("Salida del sistema")"""
    
    
    

    