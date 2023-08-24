from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363#login?authsrc=h"
page="https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver,5,poll_frequency=1)
try:
    driver.get(page)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'index-login-NV2z_')))
    href=element.get_attribute('href')

    if href==url:

        driver.find_element(By.CLASS_NAME, "desktop-usq1f1").click()
        button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-marker="item-view/favorite-button"]')))
        wait.until(lambda driver: button.get_attribute('data-is-favorite') == "true")

        if button.get_attribute('data-is-favorite') == "true":
            print("success")

    elif href=="https://www.avito.ru/profile":

        print("You are logged in, log out")

except Exception as ex:
    print(ex)

finally:

    driver.close()
    driver.quit()