import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_catalogo():
    

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



        # Valido título de la pestaña de Chrome
        assert driver.title == "Swag Labs"
        print("\n✓ Título de la pestaña correcto")

        # Compruebo que exista al menos un item cargado en la pagina
        productos = driver.find_elements(By.CSS_SELECTOR,"a[id^='item_'][id$='_title_link']")

        assert len(productos) >= 1, "No se encontró ningún producto cargado"
        print("\n✓ Al menos 1 producto mostrado correcto")

        productosCant = driver.find_elements(By.CLASS_NAME,"inventory_item")
        cant = len(productosCant)
        assert cant > 0
        print(f"\n✓ {cant} producto/s mostrado/s correcto")

        # Compruebo la existencia de boton hamburguesa
        boton_menu = driver.find_elements(By.ID,"react-burger-menu-btn")

        assert len(boton_menu) >= 1, "No se encontró el botón Open Menu"
        print("\n✓ Boton hamburguesa mostrado correcto")


    finally:
        driver.quit()