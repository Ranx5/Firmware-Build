
#!/bin/bash
# 添加luci-app-mosdns
#rm -rf feeds/packages/net/v2ray-geodata
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-mihomo
git clone --depth=1 https://github.com/morytyann/OpenWrt-mihomo.git -b main package/luci-app-mihomo
# 添加luci-app-passwall
rm -rf feeds/luci/applications/luci-app-passwall
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall.git -b main package/luci-app-passwall
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall-packages.git -b main package/passwall-packages
# 添加luci-app-passwall2
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall2.git -b main package/luci-app-passwall2
# 添加luci-app-amlogic
git clone --depth=1 https://github.com/ophub/luci-app-amlogic.git -b main package/luci-app-amlogic
