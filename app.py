from flask import Flask
from selenium import webdriver
import time

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

@app.route('/')
def index():
    # 在請求處理函數內部使用 WebDriver
    driver = get_driver()
    driver.get("https://www.example.com")
    time.sleep(5)
    title = driver.title  # 取得網頁標題
    driver.quit()
    return title

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
