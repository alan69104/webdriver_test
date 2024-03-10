#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -nv -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  echo "...Extracting Chrome package"
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  # Find the version of the extracted Chrome
  CHROME_VERSION=$(grep -Po '(?<=^Version=).+' $STORAGE_DIR/chrome/opt/google/chrome/chrome)
  echo "Installed Chrome version: $CHROME_VERSION"
  cd - # Make sure we return to where we were
else
  echo "...Using Chrome from cache"
fi

# be sure to add Chrome's location to the PATH as part of your Start Command
export PATH="${PATH}:${STORAGE_DIR}/chrome/opt/google/chrome"

# add your own build commands...
