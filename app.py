from selenium import webdriver
import time
import os
from flask import Flask

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

driver = get_driver()

# 打開網頁
driver.get("https://www.example.com")

# 等待一段時間
time.sleep(5)

# 關閉瀏覽器
driver.quit()

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
