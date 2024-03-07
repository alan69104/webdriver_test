# 載入需要的套件
from flask import Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)

@app.route('/')
def index():
    # 使用 webdriver-manager 自動下載和管理 Chrome webdriver
    driver = webdriver.Chrome()

    # 連到我的網站
    driver.get("https://kirin.idv.tw")

    # 印出網頁的標題
    title = driver.title

    # 關閉瀏覽器
    driver.quit()

    return title

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
