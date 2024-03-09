from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask
from selenium import webdriver

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def get_page_title(url):
    driver = get_driver()
    if driver is None:
        return "無法建立 WebDriver"

    try:
        driver.get(url)
        # 使用顯式等待等待頁面標題出現
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        page_title = driver.title
        return page_title
    except Exception as e:
        print("獲取頁面標題時發生錯誤:", e)
        return "無法獲取頁面標題"
    finally:
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print("退出 WebDriver 時發生錯誤:", e)

@app.route('/')
def index():
    url = "https://www.example.com"  # 設置要獲取標題的網頁URL
    page_title = get_page_title(url)
    return f"頁面標題: {page_title}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
