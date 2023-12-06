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
from altaEmpleado import test_altaEmployee
from consultaEmpleado import test_consultaEmployee

service = Service("C:/Chromedriver/chromedriver.exe")

def test_piloto():
    test_altaEmployee()
    test_consultaEmployee()

if __name__ == "__main__":
    test_piloto()
 
