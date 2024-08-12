from config_selenium import *
from scripts.private_credentials import *

def login_jira():
    driver.get("https://siman.atlassian.net/jira/software/c/projects/CSC/boards/115/backlog");

    time.sleep(2)

    btn_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "microsoft-auth-button")))
    btn_login.click()


    input_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "i0116")))
    input_email.send_keys(email)

    btn_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    btn_next.click()

    input_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "i0118")))
    input_password.send_keys(password)

    btn_sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    btn_sign_in.click()

    btn_sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    btn_sign_in.click()
