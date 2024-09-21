#!/bin/bash
# 修改默认IP
# sed -i 's/192.168.1.1/192.168.32.1/g' package/base-files/files/bin/config_generate
# 添加luci-app-mosdns
rm -rf feeds/packages/net/v2ray-geodata
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
git clone https://github.com/sbwml/v2ray-geodata package/v2ray-geodata
old_perms=$(stat -c %a package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns)
echo $old_perms
rm -f package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns
wget -cO package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/mosdns
chmod $old_perms package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-mihomo
git clone --depth=1 https://github.com/morytyann/OpenWrt-mihomo.git -b main package/luci-app-mihomo
# 添加luci-app-passwall
rm -rf feeds/luci/applications/luci-app-passwall
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall.git -b main package/luci-app-passwall
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall-packages.git -b main package/passwall-packages
# 添加luci-app-homeproxy
rm -rf feeds/luci/applications/luci-app-homeproxy
git clone --depth=1 https://github.com/douglarek/luci-app-homeproxy.git package/luci-app-homeproxy
# 更换Ruby
rm -rf feeds/packages/lang/ruby
mkdir ruby && chmod -R 777 ruby
git clone https://github.com/immortalwrt/packages.git -b master ruby
# cd ruby && git checkout f5e5fe7ad280f28b6800ee69c1b1e88ce58f08cd
cd ruby && git checkout 39c14b859abc0fdbe9a6bea112e9cc5b0406f753
cd ..
cp -rf ruby/lang/ruby feeds/packages/lang/ruby
rm -rf ruby
