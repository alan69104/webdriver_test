#!/usr/bin/env bash
# exit on error
set -o errexit -o pipefail

STORAGE_DIR=/opt/render/project/.render

function log_error {
  echo "ERROR: $1" >&2
  exit 1
}

echo "Starting deployment..."

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -nv -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb || log_error "Chrome download failed"
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome || log_error "dpkg extract failed"
  rm ./google-chrome-stable_current_amd64.deb
  cd - # Return to the previous directory
else
  echo "...Using Chrome from cache"
fi

# Set Chrome's location to the PATH
CHROME_DIR=$STORAGE_DIR/chrome/opt/google/chrome
export PATH=$PATH:$CHROME_DIR

echo "Checking Chrome version..."
CHROME_VERSION=$(google-chrome --product-version | cut -d '.' -f 1-3) || log_error "Chrome version check failed"
echo "Detected Chrome version: $CHROME_VERSION"

echo "Checking if ChromeDriver is already installed..."
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading ChromeDriver"
  CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") || log_error "ChromeDriver version fetch failed"
  if [[ -z "$CHROMEDRIVER_VERSION" ]]; then
    log_error "Failed to fetch ChromeDriver version for Chrome version $CHROME_VERSION"
  fi
  echo "Detected ChromeDriver version: $CHROMEDRIVER_VERSION"
  CHROMEDRIVER_URL="https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
  echo "Downloading ChromeDriver from: $CHROMEDRIVER_URL"
  wget -nv -P $STORAGE_DIR "$CHROMEDRIVER_URL" || log_error "ChromeDriver download failed"
  unzip -q $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR || log_error "Unzip failed"
  chmod +x $STORAGE_DIR/chromedriver
  rm $STORAGE_DIR/chromedriver_linux64.zip
  echo "ChromeDriver installed successfully."
else
  echo "...Using ChromeDriver from cache"
fi

# Set ChromeDriver's location to the PATH
export PATH=$PATH:$STORAGE_DIR

echo "Deployment script finished."
# add your own build commands...
