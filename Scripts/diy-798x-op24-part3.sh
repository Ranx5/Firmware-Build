#!/bin/bash
cp -af ./feeds/mtk_openwrt_feed/24.10/files/* .
for file in $(find ./feeds/mtk_openwrt_feed/24.10/patches-base -name "*.patch" | sort); do patch -f -p1 -i ${file}; done
