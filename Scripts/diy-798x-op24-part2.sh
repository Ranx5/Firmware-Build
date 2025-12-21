#!/bin/bash
# 添加luci-app-mosdns
#rm -rf feeds/packages/net/v2ray-geodata
rm -rf feeds/packages/lang/golang
git clone https://github.com/sbwml/packages_lang_golang -b 24.x feeds/packages/lang/golang
rm -rf feeds/packages/net/mosdns
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
#git clone https://github.com/sbwml/v2ray-geodata package/v2ray-geodata
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# sed -i 's/--set=llvm\.download-ci-llvm=true/--set=llvm.download-ci-llvm=if-unchanged/' feeds/packages/lang/rust/Makefile
# 添加luci-app-nikki
git clone --depth=1 https://github.com/nikkinikki-org/OpenWrt-nikki.git -b main package/luci-app-nikki
# 添加luci-theme-argon
git clone --depth=1 https://github.com/jerrykuku/luci-theme-argon.git -b master package/luci-theme-argon
# 添加luci-app-argon-config
git clone --depth=1 https://github.com/jerrykuku/luci-app-argon-config.git -b master package/luci-app-argon-config
# 应用补丁
cp -af ./feeds/mtk_openwrt_feed/24.10/files/* .
for file in $(find ./feeds/mtk_openwrt_feed/24.10/patches-base -name "*.patch" | sort); do patch -f -p1 -i ${file}; done
