from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service('/path/to/chromedriver')  # 請替換為你的 ChromeDriver 路徑
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@app.route('/')
def index():
    # 在請求處理函數內部使用 WebDriver
    driver = get_driver()
    driver.get("https://www.example.com")
    
    # 等待網頁完全加載
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    title = driver.title  # 取得網頁標題
    driver.quit()
    return title

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
