#!/bin/bash
echo "src-git mtk_openwrt_feed https://git01.mediatek.com/openwrt/feeds/mtk-openwrt-feeds" >> feeds.conf.default
./scripts/feeds update -a
./scripts/feeds install -a
