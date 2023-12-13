import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException, UnexpectedTagNameException
from selenium.webdriver import ActionChains
import logging

class Funciones_Globales():
    def __init__(self,driver):
        self.driver = driver
        self.configure_logging()

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t
    
    def Navegar(self,url,tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Page open:"+ url)
        t=time.sleep(tiempo)
        return t
    
    def SX(self, selector):
        val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,selector)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, selector)
        
        return val
    
    def SID(self, selector):
        val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.ID,selector)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, selector)
        return val


    
    def text_val(self,tipo,selector,texto,tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SX(selector)
                val.clear()
                val.send_keys(texto)
                print("escribiendo en el campo: {} en el texto: {}".format(selector,texto), flush=True)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no encontrado:"+ selector)
        elif(tipo=="id"):
            try:
                val = self.SID(selector)
                val.clear()
                val.send_keys(texto)
                print("escribiendo en el campo: {} en el texto: {}".format(selector,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no encontrado:"+ selector)
            
            
    def click_val(self,tipo,selector,tiempo):
        if(tipo=="xpath"):  
            try:
                val = self.SX(selector)
                val.click()
                print("click en el campo {}".format(selector), flush=True)
                t = time.sleep(tiempo)
                return t
        
            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no encontrado:"+ selector)
        elif(tipo=="id"):
            try:
                val = self.SID(selector)
                val.click()
                print("click en el campo {}".format(selector))
                t = time.sleep(tiempo)
                return t
        
            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no encontrado:"+ selector)


    def select_xpath_type(self,xpath,tipo,dato,tiempo):
        try:
            val= WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By. XPATH, xpath)))
            val= self.driver.find_element(By. XPATH, xpath)
            val= Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            print("El campo seleccionado es {}".format(dato))
            t= time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def upload_xpath(self,xpath,ruta,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("se carga imagen {}".format(ruta))
            t = time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def check_xpath(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return  t
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def check_xpath_mult(self,tiempo, *args):
        try:
            for num in args:    
                val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("click en el elemento {}".format(num))
                t = time.sleep(tiempo)
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("elemento no encontrado:"+ num)

    def Existe(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("El elemento {} -> Existe".format(xpath))
            t = time.sleep(tiempo)
            return "Existe"
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no existe:" + xpath)  


    def Mouse_Doble(self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = self.driver.find_element(By. XPATH, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val = self.SID(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t      
        else:
            print("Selector desconocido")

    def Mouse_Derecho(self,tipo,selector,tiempo=.2):
        if(tipo=="xpath"):
            try:
                val=self.SX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif(tipo == "id"):
            try:
                val = self.driver.find_element(By. ID, selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
            
    def Mouse_DragDrop(self, tipo, selector,destino, tiempo=.2):
        if (tipo == "xpath"):
            try:
                val = self.SX(selector)
                val2=self.SX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SID(selector)
                val2 = self.SID(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
    def Mouse_DragDropXY(self, tipo, selector,x,y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SID(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
            
    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SID(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def scroll_into_view(self, selector):
        val = self.driver.find_element(By.XPATH, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", val)


    def configure_logging(self, logger_name=__name__):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(logger_name)

    def select_type(self, xpath, tipo, dato, tiempo):
        try:
        # Esperar a que el elemento sea visible
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Intentar crear un objeto Select (funcionará para elementos select)
            try:
                val = Select(val)
            except UnexpectedTagNameException:
                pass  # No es un elemento select, continuará con el elemento original

            if tipo == "text":
                if isinstance(val, Select):
                    val.select_by_visible_text(dato)
                else:
                # Si no es un elemento select, intentar escribir directamente el texto
                    val.clear()
                    val.send_keys(dato)
            elif tipo == "value":
                if isinstance(val, Select):
                    val.select_by_value(dato)
                else:
                # Si no es un elemento select, intentar escribir directamente el valor
                    val.clear()
                    val.send_keys(dato)
            elif tipo == "index":
                if isinstance(val, Select):
                    val.select_by_index(dato)
                else:
                # Si no es un elemento select, intentar escribir directamente el índice
                    val.clear()
                    val.send_keys(str(dato))

            print("El campo seleccionado es {}".format(dato))
            time.sleep(tiempo)

        except TimeoutException as ex:
            print(ex.msg)
            print("Elemento no encontrado: " + xpath)