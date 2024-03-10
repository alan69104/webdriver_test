#!/usr/bin/env bash

# 遇到錯誤時終止腳本
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
    echo "正在下載 Chrome..."
    mkdir -p $STORAGE_DIR/chrome
    cd $STORAGE_DIR/chrome
    wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
    rm ./google-chrome-stable_current_amd64.deb
    cd $HOME/project/src # 確保我們返回到原本的位置
    echo "Chrome 安裝完成。"
else
    echo "從快取中使用 Chrome。"
fi

# 設置 Chrome 執行路徑到環境變數
CHROME_PATH="/opt/render/project/.render/chrome/opt/google/chrome/chrome"
export CHROME_PATH
export PATH="$PATH:$CHROME_PATH"

# 安裝 ChromeDriver
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
    echo "正在下載 ChromeDriver..."
    CHROME_DRIVER_VERSION=$(google-chrome --product-version)
    wget -P $STORAGE_DIR https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
    unzip $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR
    rm $STORAGE_DIR/chromedriver_linux64.zip
    echo "ChromeDriver 安裝完成。"
else
    echo "從快取中使用 ChromeDriver。"
fi

# 設置 ChromeDriver 執行路徑到環境變數
CHROME_DRIVER_PATH="$STORAGE_DIR/chromedriver"
export CHROME_DRIVER_PATH

# 調試信息
echo "CHROME_PATH 設置為: $CHROME_PATH"
ls -l "$CHROME_PATH"
which chrome
echo "CHROME_DRIVER_PATH 設置為: $CHROME_DRIVER_PATH"
ls -l "$CHROME_DRIVER_PATH"

mkdir -p /tmp
# 在此添加您自己的構建命令...
