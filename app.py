# 載入需要的套件
from flask import Flask
from selenium import webdriver
import os

app = Flask(__name__)

@app.route('/')
def index():
    # 建立一個Chrome的webdriver物件，並指定driver的路徑
    browser = webdriver.Chrome(executable_path=os.environ['PATH'] + ":/opt/render/project/.render/chrome/opt/google/chrome/")

    # 連到我的網站
    browser.get("https://kirin.idv.tw")

    # 印出網頁的標題
    title = browser.title

    # 關閉瀏覽器
    browser.quit()

    return title

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
