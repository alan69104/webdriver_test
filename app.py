from flask import Flask, render_template
from selenium import webdriver
import time

app = Flask(__name__)

@app.route('/')
def index():
    # 使用 Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 在無頭模式下運行，不顯示實際瀏覽器窗口
    driver = webdriver.Chrome(options=options)

    # 打開網頁
    driver.get("https://www.example.com")

    # 等待一段時間
    time.sleep(5)

    # 獲取網頁內容，此處只是示例
    page_content = driver.page_source

    # 關閉瀏覽器
    driver.quit()

    return render_template('index.html', content=page_content)

if __name__ == "__main__":
    app.run()

