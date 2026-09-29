import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_carrito():
    

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

        #  Compruebo la existencia de boton carrito
        carrito = driver.find_elements(By.CSS_SELECTOR,"a[data-test='shopping-cart-link']")

        assert len(carrito) >= 1, "No se encontró el botón del carrito"
        print("\n✓ Boton carrito mostrado correcto")

        # Compruebo que el filtro sea visible
        filtro = driver.find_element(By.CSS_SELECTOR,"select[data-test='product-sort-container']")

        assert filtro.is_displayed(), "El filtro de productos no está visible"
        print("\n✓ Filtro visible correcto")

        # Compruebo que al añadir un producto al carrito el contador de este se incrementa
        # Comprobar que inicialmente el carrito está vacío
        carrito = driver.find_elements(
            By.CSS_SELECTOR,
            "span[data-test='shopping-cart-badge']"
        )

        assert len(carrito) == 0, "El carrito no está vacío inicialmente"
        print("\n✓ El carrito se encuentra en 0 items correcto")

        # Agregar un producto
        boton_agregar = driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        boton_agregar.click()

        # input("Presiona una tecla... Aumentar el numero de items manualmente en el carrito para que falle.")

        # Obtener cantidad de productos en el carrito
        carrito = driver.find_element(
            By.CSS_SELECTOR,
            "span[data-test='shopping-cart-badge']"
        )

        cantidad = int(carrito.text)

        # Verificar que ahora hay 1 producto
        assert cantidad == 1, f"Se esperaba 1 producto, pero hay {cantidad}"
        print("\n✓ El carrito tiene 1 item correcto")


        # input("Presiona una tecla...")


        # Navegar el carrito de compras
        carrito = driver.find_element(By.CSS_SELECTOR,"a[data-test='shopping-cart-link']")
        carrito.click()

        assert driver.current_url == "https://www.saucedemo.com/cart.html"
        print("\n✓ URL del carrito correcta")

        # Compruebo que el Sauce Labs Backpack esta en el carrito
        producto = driver.find_elements(By.CSS_SELECTOR,"div[data-test='inventory-item-name']")

        nombres = [item.text for item in producto]

        assert "Sauce Labs Backpack" in nombres, \
        "Sauce Labs Backpack no se encuentra en el carrito"
        print("\n✓ El item de prueba fue encontrado en el carrito correcta")



    finally:
        driver.quit()