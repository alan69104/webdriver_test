#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd - # Return to the previous directory
else
  echo "...Using Chrome from cache"
fi

# Set Chrome's location to the PATH
CHROME_DIR=$STORAGE_DIR/chrome/opt/google/chrome
export PATH=$PATH:$CHROME_DIR

# Check Chrome version
CHROME_VERSION=$(google-chrome --product-version | cut -d '.' -f 1-3)
echo "Detected Chrome version: $CHROME_VERSION"

# Install ChromeDriver
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading ChromeDriver"
  CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
  if [[ -z "$CHROMEDRIVER_VERSION" ]]; then
    echo "Failed to fetch ChromeDriver version for Chrome version $CHROME_VERSION"
    exit 1
  fi
  echo "Detected ChromeDriver version: $CHROMEDRIVER_VERSION"
  wget -P $STORAGE_DIR https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
  unzip $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR
  chmod +x $STORAGE_DIR/chromedriver
  rm $STORAGE_DIR/chromedriver_linux64.zip
else
  echo "...Using ChromeDriver from cache"
fi

# Set ChromeDriver's location to the PATH
export PATH=$PATH:$STORAGE_DIR

# add your own build commands...
