#!/bin/bash
# 修改feeds.conf.default
sed -i '/openwrt-23/d' feeds.conf.default
sed -i '/#.*luci/s/^#//' feeds.conf.default
# 更新feed
./scripts/feeds update -a
./scripts/feeds install -a
