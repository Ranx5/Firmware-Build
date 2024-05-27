#!/bin/bash
# Add a feed source
# echo 'src-git passwall2_packages https://github.com/xiaorouji/openwrt-passwall-packages.git' >> feeds.conf.default
# echo 'src-git passwall2 https://github.com/xiaorouji/openwrt-passwall2.git' >> feeds.conf.default
./scripts/feeds update -a
./scripts/feeds install -a
