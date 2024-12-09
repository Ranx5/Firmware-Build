#!/bin/bash
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
# 更换Ruby
rm -rf feeds/packages/lang/ruby
mkdir ruby && chmod -R 777 ruby
git clone https://github.com/immortalwrt/packages.git -b master ruby
# cd ruby && git checkout f5e5fe7ad280f28b6800ee69c1b1e88ce58f08cd
cd ruby && git checkout 39c14b859abc0fdbe9a6bea112e9cc5b0406f753
cd ..
cp -rf ruby/lang/ruby feeds/packages/lang/ruby
rm -rf ruby
