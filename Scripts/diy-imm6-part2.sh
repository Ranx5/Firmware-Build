
#!/bin/bash
# 修改默认IP
sed -i 's/192.168.1.1/192.168.32.1/g' package/base-files/files/bin/config_generate
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
# 添加luci-app-passwall2
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall-packages.git package/passwall-packages
git clone --depth=1 https://github.com/xiaorouji/openwrt-passwall2.git package/luci-app-passwall2
# 更换dst
rm -f package/boot/uboot-envtools/files/mediatek_filogic
wget -cO package/boot/uboot-envtools/files/mediatek_filogic https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/rax3000m/mediatek_filogic
wget -cO target/linux/mediatek/dts/mt7981b-cmcc-rax3000m-nand-ubootmod.dts https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/rax3000m/mt7981b-cmcc-rax3000m-nand-ubootmod.dts
rm -f target/linux/mediatek/filogic/base-files/etc/board.d/02_network
wget -cO target/linux/mediatek/filogic/base-files/etc/board.d/02_network https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/rax3000m/02_network
rm -f target/linux/mediatek/filogic/base-files/etc/hotplug.d/ieee80211/11_fix_wifi_mac
wget -cO target/linux/mediatek/filogic/base-files/etc/hotplug.d/ieee80211/11_fix_wifi_mac https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/rax3000m/11_fix_wifi_mac
rm -f target/linux/mediatek/image/filogic.mk
wget -cO target/linux/mediatek/image/filogic.mk https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/rax3000m/filogic.mk
