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
# 添加luci-app-argon
git clone --depth=1 https://github.com/jerrykuku/luci-theme-argon.git -b master package/luci-theme-argon
git clone --depth=1 https://github.com/jerrykuku/luci-app-argon-config.git -b master package/luci-app-argon-config
# 修改dst
wget -cO target/linux/qualcommax/files/arch/arm64/boot/dts/qcom/ipq6018-ax18.dts https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/ipq6018-ax18.dts
wget -cO target/linux/qualcommax/files/arch/arm64/boot/dts/qcom/ipq6018-cmiot.dtsi https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/ipq6018-cmiot.dtsi
wget -cO target/linux/qualcommax/files/arch/arm64/boot/dts/qcom/ipq6018-cpufreq.dtsi https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/ipq6018-cpufreq.dtsi
wget -cO target/linux/qualcommax/files/arch/arm64/boot/dts/qcom/ipq6018-m2.dts https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/ipq6018-m2.dts
rm -f target/linux/qualcommax/image/ipq60xx.mk
wget -cO target/linux/qualcommax/image/ipq60xx.mk https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/ipq60xx.mk
wget -cO package/firmware/ipq-wifi/src/board-cmiot_ax18.ipq6018 https://github.com/Ranx5/Firmware-Build/blob/main/Defconfig/ipq6000/board-cmiot_ax18.ipq6018
wget -cO package/firmware/ipq-wifi/src/board-zn_m2.ipq6018 https://github.com/Ranx5/Firmware-Build/blob/main/Defconfig/ipq6000/board-zn_m2.ipq6018
rm -f package/firmware/ipq-wifi/Makefile
wget -cO package/firmware/ipq-wifi/Makefile https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/Makefile
rm -f package/boot/uboot-envtools/files/qualcommax_ipq60xx
wget -cO package/boot/uboot-envtools/files/qualcommax_ipq60xx https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/qualcommax_ipq60xx
rm -f target/linux/qualcommax/ipq60xx/base-files/etc/board.d/01_leds
wget -cO target/linux/qualcommax/ipq60xx/base-files/etc/board.d/01_leds https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/01_leds
rm -f target/linux/qualcommax/ipq60xx/base-files/etc/board.d/02_network
wget -cO target/linux/qualcommax/ipq60xx/base-files/etc/board.d/02_network https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/02_network
rm -f target/linux/qualcommax/ipq60xx/base-files/etc/hotplug.d/firmware/11-ath11-caldata
wget -cO target/linux/qualcommax/ipq60xx/base-files/etc/hotplug.d/firmware/11-ath11-caldata https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/11-ath11-caldata
rm -f target/linux/qualcommax/ipq60xx/base-files/lib/upgrade/platform.sh
wget -cO target/linux/qualcommax/ipq60xx/base-files/lib/upgrade/platform.sh https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/ipq6000/platform.sh


