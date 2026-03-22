import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def criar_driver():
    opcoes = Options()
    opcoes.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    opcoes.add_argument("--disable-notifications")
    opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=opcoes)

driver = criar_driver()

# Entrando no saucedemo e testando os logins com os usuários
driver.get("https://www.saucedemo.com/")

# Lista com os users para login
lista_user = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

# Loop mexendo nos usuários e dando logout logo em seguida (testar todos users)
for user in lista_user:
    username_login = driver.find_element(By.XPATH, '//*[@type="text"]')
    password_login = driver.find_element(By.XPATH, '//*[@type="password"]')
    botao_login = driver.find_element(By.XPATH, '//*[@type="submit"]')
    
    username_login.send_keys(user)
    password_login.send_keys("secret_sauce")
    time.sleep(2)
    botao_login.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    time.sleep(2)
    menu_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_btn.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='bm-item-list']"))
    )
    logout_homepage = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
    logout_homepage.click()
    time.sleep(3)

print("Automação concluida...")






