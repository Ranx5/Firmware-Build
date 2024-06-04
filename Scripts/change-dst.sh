
#!/bin/bash
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
