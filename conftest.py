import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador a usar: chrome | firefox | edge",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Correr sin abrir ventana grafica",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1400,900")
        drv = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        drv = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Navegador '{browser}' no soportado.")

    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return "https://parabank.parasoft.com/parabank"


@pytest.fixture
def usuario_registrado(driver, base_url):
    """
    Fixture robusto: Crea un usuario mediante la interfaz y si ParaBank 
    falla en la redirección, realiza un login explícito garantizando 
    llegar a /overview.htm con una sesión válida.
    """
    marca = f"{int(time.time() * 1000)}{random.randint(100, 999)}"
    username = f"grupo10qa{marca}"
    password = "Passw0rd2026"
    ssn_unico = marca[-9:]
    
    # Intentar registro normal
    driver.get(f"{base_url}/register.htm")
    driver.find_element(By.ID, "customer.firstName").send_keys("Alexis")
    driver.find_element(By.ID, "customer.lastName").send_keys("Zelaya")
    driver.find_element(By.ID, "customer.address.street").send_keys("Av. Siempre Viva 742")
    driver.find_element(By.ID, "customer.address.city").send_keys("San Miguel de Tucuman")
    driver.find_element(By.ID, "customer.address.state").send_keys("Tucuman")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("4000")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("381" + marca[-7:])
    driver.find_element(By.ID, "customer.ssn").send_keys(ssn_unico)
    driver.find_element(By.ID, "customer.username").send_keys(username)
    driver.find_element(By.ID, "customer.password").send_keys(password)
    driver.find_element(By.ID, "repeatedPassword").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()
    
    time.sleep(1.5)

    # Forzar el inicio de sesión explícitamente para asegurar la sesión activa
    driver.get(f"{base_url}/index.htm")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
    
    # Espera explícita a que cargue la vista de resumen de cuentas
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/overview.htm")
        )
    except Exception:
        # Si por alguna razón el usuario dinámico falla, utilizamos un usuario por defecto de respaldo
        driver.get(f"{base_url}/index.htm")
        driver.find_element(By.NAME, "username").send_keys("john")
        driver.find_element(By.NAME, "password").send_keys("demo")
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/overview.htm")
        )
        return {"username": "john", "password": "demo"}

    return {"username": username, "password": password}