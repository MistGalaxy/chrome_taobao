from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#加表头
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(chrome_options=options)
wait=WebDriverWait(browser,10)

def search():


    browser.get('https://www.taobao.com')
    input=wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#q'))
    )

    submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    input[0].send_keys('美食')
    submit.click()




def main():
    search()

if __name__=='__main__':
    main()
