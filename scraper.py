from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://hprera.nic.in/PublicDashboard')

wait = WebDriverWait(driver, 20)
project_links = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@onclick, 'tab_project_main_ApplicationPreview')]"))
)

for i, project in enumerate(project_links[:6]):
    
    ActionChains(driver).move_to_element(project).click().perform()
    time.sleep(2)  

    
    try:

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[text()='Name']/following-sibling::td"))
        )
        name = driver.find_element(By.XPATH, "//td[text()='Name']/following-sibling::td").text
        pan_no = driver.find_element(By.XPATH, "//td[text()='PAN No.']/following-sibling::td").text
        permanent_address = driver.find_element(By.XPATH, "//td[text()='Permanent Address']/following-sibling::td").text
        gstin_no = driver.find_element(By.XPATH, "//td[text()='GSTIN No.']/following-sibling::td").text

        print(f"Project {i + 1}:")
        print(f"Name: {name}")
        print(f"PAN No: {pan_no}")
        print(f"Permanent Address: {permanent_address}")
        print(f"GSTIN No: {gstin_no}")
        print("-" * 30)

    except Exception as e:
        print(f"Could not extract details for project {i + 1}: {e}")

  
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, "button[data-dismiss='modal']")
        close_button.click()
    except Exception as e:
        print(f"Could not find or click the close button: {e}")

    time.sleep(1)


driver.quit()
