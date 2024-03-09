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
    driver = None
    try:
        driver = get_driver()
        driver.get("https://www.example.com")
        time.sleep(5)
        title = driver.title  # 取得網頁標題
        return title
    except Exception as e:
        return f"Error occurred: {str(e)}"
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
