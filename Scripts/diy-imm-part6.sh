#!/bin/bash
# 添加luci-app-mosdns
#rm -rf feeds/packages/net/v2ray-geodata
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
#git clone https://github.com/sbwml/v2ray-geodata package/v2ray-geodata
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-mihomo
git clone --depth=1 https://github.com/morytyann/OpenWrt-mihomo.git -b main package/luci-app-mihomo
# 添加luci-app-passwall2
rm -rf feeds/packages/net/{chinadns*,hysteria,geoview,trojan*,xray*,v2ray*,sing*, mosdns}
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall-packages.git -b main package/passwall-packages
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall2.git -b main package/luci-app-passwall2
