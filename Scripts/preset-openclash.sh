#!/bin/bash

mkdir -p files/etc/openclash/core
mkdir -p files/etc/config
mkdir -p files/etc/openclash/custom
mkdir -p files/etc/uci-defaults
# mkdir -p files/etc/mosdns
# mkdir -p files/etc/init.d

# CLASH_META_URL="https://raw.githubusercontent.com/vernesong/OpenClash/core/master/meta/clash-linux-arm64.tar.gz"
GEOIP_URL="https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geoip.dat"
GEOSITE_URL="https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geosite.dat"
CLASH_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/openclash.config"
CONFIG_MODIFY_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/modify_uv.py"
MOSDNS_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/mosdns.config"
ANTI_AD_URL="https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/adblock-for-dnsmasq.conf"
CUSTOM_FIREWALL_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/main/Scripts/openclash_custom_firewall_rules.sh"
UCI_DEFAULT_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Scripts/99z-default-setting.sh"
# MOSDNS_CUSTOM_URL="https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build-Lean/main/clash/mosdns2.yaml"
# MOSDNS_GEN_URL="https://raw.githubusercontent.com/Unwillingx/OpenWrt-Build/main/Configs/mosdns"

# wget -qO- $CLASH_META_URL | tar xOvz > files/etc/openclash/core/clash_meta
# 获取仓库的最新发布信息
release_info=$(wget -qO- https://api.github.com/repos/MetaCubeX/mihomo/releases/latest)
# 解析JSON以获取最新发布的tag
tag=$(echo "$release_info" | grep -oP '"tag_name": "\K(.*?)(?=")')
echo "$tag"
# 构建文件名
file_name="mihomo-linux-arm64-$tag.gz"
echo "$file_name"
# 解析JSON以获取文件下载链接
download_url=$(echo "$release_info" | grep -oP '"browser_download_url": "\K(.*?)(?=")' | grep "$file_name")
echo "$download_url"
# 下载文件
if [ -n "$download_url" ]; then
    echo "Downloading latest release from: $download_url"
    wget -qO- "$download_url" | gunzip -c > files/etc/openclash/core/clash_meta
    echo "Download complete."
else
    echo "Failed to retrieve download URL for $file_name."
fi

wget -qO- $GEOIP_URL > files/etc/openclash/GeoIP.dat
wget -qO- $GEOSITE_URL > files/etc/openclash/GeoSite.dat
wget -qO- $CLASH_CONFIG_URL > files/etc/config/openclash
wget -qO- $ANTI_AD_URL > files/etc/openclash/anti-ad-for-dnsmasq.conf
wget -qO- $CUSTOM_FIREWALL_URL > files/etc/openclash/custom/openclash_custom_firewall_rules.sh
wget -qO- $CONFIG_MODIFY_URL > files/etc/openclash/modify_uv.py
wget -qO- $MOSDNS_CONFIG_URL > files/etc/config/mosdns
wget -qO- $UCI_DEFAULT_URL > files/etc/uci-defaults/99z-default-setting.sh
# wget -qO- $MOSDNS_CUSTOM_URL > files/etc/mosdns/config_custom.yaml
# wget -qO- $MOSDNS_GEN_URL > files/etc/init.d/mosdns

chmod +x files/etc/openclash/core/clash*
chmod +x files/etc/openclash/modify_uv.py
chmod +x files/etc/uci-defaults/99z-default-setting.sh
chmod +x files/etc/openclash/custom/openclash_custom_firewall_rules.sh
chmod +rw files/etc/openclash/anti-ad-for-dnsmasq.conf
chmod +rw files/etc/config/openclash
chmod +rw files/etc/config/mosdns
# chmod +rw files/etc/mosdns/config_custom.yaml
# chmod +rwx files/etc/init.d/mosdns
