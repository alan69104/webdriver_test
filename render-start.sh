#!/usr/bin/env bash
# 出錯時退出
set -o errexit -o pipefail

STORAGE_DIR=/opt/render/project/.render

function log_error {
  echo "錯誤：$1" >&2
  exit 1
}

echo "開始部署..."

# 定義 Chrome 的下載 URL
CHROME_DOWNLOAD_URL="https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/linux64/chrome-linux64.zip"
echo "...正在下載指定版本的 Chrome"
mkdir -p $STORAGE_DIR/chrome
cd $STORAGE_DIR/chrome
wget -nv "$CHROME_DOWNLOAD_URL" || log_error "Chrome 下載失敗"
unzip -o -q chrome-linux64.zip || log_error "解壓失敗" # 使用 -o 選項自動覆蓋檔案
rm chrome-linux64.zip
cd - # 返回之前的目錄

# 假設解壓後的 Chrome 可執行檔案位於當前目錄
CHROME_DIR=$STORAGE_DIR/chrome
export PATH=$PATH:$CHROME_DIR

echo "偵測到的 Chrome 版本：122.0.6261.111"

# 下載並安裝 ChromeDriver
CHROMEDRIVER_DOWNLOAD_URL="https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/linux64/chromedriver-linux64.zip"
echo "...正在下載指定版本的 ChromeDriver"
wget -nv -P $STORAGE_DIR "$CHROMEDRIVER_DOWNLOAD_URL" || log_error "ChromeDriver 下載失敗"
unzip -q $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR || log_error "解壓失敗"
chmod +x $STORAGE_DIR/chromedriver
rm $STORAGE_DIR/chromedriver_linux64.zip
echo "ChromeDriver 安裝成功。"

# 將 ChromeDriver 的位置添加到 PATH
export PATH=$PATH:$STORAGE_DIR

echo "部署腳本執行完畢。"
