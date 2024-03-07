from selenium import webdriver
import time
import os

# 使用 Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 在無頭模式下運行，不顯示實際瀏覽器窗口
driver = webdriver.Chrome(options=options)

# 打開網頁
driver.get("https://www.example.com")

# 等待一段時間
time.sleep(5)

# 關閉瀏覽器
driver.quit()
