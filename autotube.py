from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = input("Enter your full name: ")
email = input("Enter your existing email (lost access): ")
password = input("Enter your desired password for the new account: ")
dob = input("Enter your date of birth in DD/MM/YYYY format: ")

day, month, year = dob.split("/")

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)

# Access YouTube signup page
driver.get("https://www.youtube.com/create_account")

wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds

wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(name.split()[0])
wait.until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(name.split()[1])
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
wait.until(EC.presence_of_element_located((By.ID, "month"))).send_keys(month)
wait.until(EC.presence_of_element_located((By.ID, "day"))).send_keys(day)
wait.until(EC.presence_of_element_located((By.ID, "year"))).send_keys(year)

# Optional: Select sex (uncomment if needed)
# sex_select = wait.until(EC.presence_of_element_located((By.ID, "gender")))
# sex_select.click()
# desired_sex_option = sex_select.find_element(By.CSS_SELECTOR, "option[value='male']")  # Or 'female'
# desired_sex_option.click()

# Agree to terms (uncomment if needed)
# terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "terms")))
# terms_checkbox.click()

# Submit form (uncomment if automatic form submission is desired)
# submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit")))
# submit_button.click()

# Important note: Creating multiple accounts or circumventing YouTube's terms is strictly against their policies and can lead to account bans. Use this script responsibly and ethically.

# Close browser (uncomment if automatic browser closing is desired)
# driver.quit()
