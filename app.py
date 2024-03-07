from selenium import webdriver
import time
import os

# 獲取環境變量中Chrome WebDriver的路徑
chrome_driver_path = os.path.join(os.getenv('PATH'), '/opt/render/project/.render/chrome/opt/google/chrome/')

# 使用 Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 打開網頁
driver.get("https://www.example.com")

# 等待一段時間
time.sleep(5)

# 關閉瀏覽器
driver.quit()
