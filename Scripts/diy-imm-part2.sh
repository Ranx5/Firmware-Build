#!/bin/bash
# 修改默认IP
sed -i 's/192.168.1.1/192.168.32.1/g' package/base-files/files/bin/config_generate
# 添加luci-app-mosdns
# rm -rf feeds/packages/net/mosdns
# find ./ | grep Makefile | grep v2ray-geodata | xargs rm -f
# find ./ | grep Makefile | grep mosdns | xargs rm -f
rm -rf feeds/packages/net/v2ray-geodata
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
git clone https://github.com/sbwml/v2ray-geodata package/v2ray-geodata
old_perms=$(stat -c %a package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns)
echo $old_perms
rm -f package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns
wget -cO package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/mosdns
chmod $old_perms package/mosdns/luci-app-mosdns/root/etc/init.d/mosdns
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-passwall2
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall-packages.git package/passwall-packages
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall2.git package/luci-app-passwall2
# 修改python
# sudo mkdir python
# sudo chmod -R 777 python
# git clone https://github.com/immortalwrt/packages.git python && cd python && git checkout c2904e115185493d3429e7e7c15e0752ce76a35f
# cd ..
# sudo rm -rf feeds/packages/lang/python
# cp -rf python/lang/python feeds/packages/lang/python
# sudo rm -rf python
# 更换dst
# rm -f package/boot/uboot-envtools/files/mediatek_filogic
# wget -cO package/boot/uboot-envtools/files/mediatek_filogic https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/mediatek_filogic
# wget -cO target/linux/mediatek/dts/mt7981b-cmcc-rax3000m-nand-ubootmod.dts https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/mt7981b-cmcc-rax3000m-nand-ubootmod.dts
# rm -f target/linux/mediatek/filogic/base-files/etc/board.d/02_network
# wget -cO target/linux/mediatek/filogic/base-files/etc/board.d/02_network https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/02_network
# rm -f target/linux/mediatek/filogic/base-files/etc/hotplug.d/ieee80211/11_fix_wifi_mac
# wget -cO target/linux/mediatek/filogic/base-files/etc/hotplug.d/ieee80211/11_fix_wifi_mac https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/11_fix_wifi_mac
# rm -f target/linux/mediatek/filogic/base-files/lib/upgrade/platform.sh
# wget -cO target/linux/mediatek/filogic/base-files/lib/upgrade/platform.sh https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/platform.sh
# rm -f target/linux/mediatek/image/filogic.mk
# wget -cO target/linux/mediatek/image/filogic.mk https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/filogic.mk
