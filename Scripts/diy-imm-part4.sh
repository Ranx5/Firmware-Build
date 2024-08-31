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
# rm -rf feeds/luci/applications/luci-app-openclash
# git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-mihomo
git clone --depth=1 https://github.com/morytyann/OpenWrt-mihomo.git -b main package/luci-app-mihomo
