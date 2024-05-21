from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def create_youtube_account(browser='chrome', proxy=None):
    name = input("Enter your full name: ")
    email = input("Enter your existing email (lost access): ")
    password = input("Enter your desired password for the new account: ")
    dob = input("Enter your date of birth in DD/MM/YYYY format: ")

    day, month, year = dob.split("/")

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        service = Service(ChromeDriverManager().install())
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
    else:
        raise ValueError("Unsupported browser. Please choose 'chrome' or 'firefox'.")

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=service, options=options)

    # Access YouTube signup page
    driver.get("https://www.youtube.com/create_account")

    wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds

    try:
        first_name, last_name = name.split()
        wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        wait.until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(last_name)
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, "month"))).send_keys(month)
        wait.until(EC.presence_of_element_located((By.ID, "day"))).send_keys(day)
        wait.until(EC.presence_of_element_located((By.ID, "year"))).send_keys(year)
    except TimeoutException as e:
        print("TimeoutException: Element not found within the specified time.")
    
    driver.quit()

if __name__ == "__main__":
    create_youtube_account(browser='chrome', proxy='your_proxy_address_here') 