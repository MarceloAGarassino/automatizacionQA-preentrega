import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    

    # Selecciono Chrome como navegador a usar y lo inicio
    driver =  webdriver.Chrome()

    try:
        # Vamos a hacer el testing de la siguiente pagina
        driver.get("https://www.saucedemo.com/")

        # Seleccionamos el elemento de la pagina (By.ID, By.TAG_NAME, By.CLASS_NAME, By.NAME) y con send_keys enviamos lo que tipeariamos en el teclado
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        # Envio el contenido a los campos 
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        # En este caso seleccionamos un button y hacemos click
        # driver.find_element(By.ID,"login-button").click()
        boton_login.click()

        # Valido URL
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        print("\n✓ URL correcta")

        # Valido titulo principal de la pagina
        logo = driver.find_element(By.CLASS_NAME,"app_logo")
        assert logo.text == "Swag Labs"
        print("\n✓ Título 'Swag Labs' correcto")

        # tambien puedo referirme a un atributo dentro de una etiqueta en este caso data-test con valor "title"
        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']") 
        assert titulo.text == "Products"
        print("\n✓ Texto 'Products' correcto")
    
    finally:
    
        driver.quit()