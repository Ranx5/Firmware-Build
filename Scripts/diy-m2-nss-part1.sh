#!/bin/bash
# Add a feed source
# echo 'src-git passwall2_packages https://github.com/xiaorouji/openwrt-passwall-packages.git' >> feeds.conf.default
# echo 'src-git passwall2 https://github.com/xiaorouji/openwrt-passwall2.git' >> feeds.conf.default
sudo mkdir tmp && sudo chmod -R 777 tmp
git clone --depth=1  https://github.com/immortalwrt/immortalwrt.git -b master tmp
sudo cp -rf tmp/package/emortal package/emortal
sudo rm -rf tmp
./scripts/feeds update -a
./scripts/feeds install -a
