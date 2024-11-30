#!/bin/bash

# 创建路径
mkdir -p files/etc/config
mkdir -p files/usr/bin
mkdir -p files/etc/mihomo

# 设置下载链接
CONFIG_MODIFY_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/mihomo_uv.py"
# MOSDNS_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/mosdns.config"
MIHOMO_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/mihomo.config"

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
    wget -qO- "$download_url" | gunzip -c > files/usr/bin/mihomo
    echo "Download complete."
else
    echo "Failed to retrieve download URL for $file_name."
fi

# 下载配置文件
wget -qO- $CONFIG_MODIFY_URL > files/etc/mihomo/modify_uv.py
# wget -qO- $MOSDNS_CONFIG_URL > files/etc/config/mosdns
wget -qO- $MIHOMO_CONFIG_URL > files/etc/config/mihomo

# 设置权限
chmod +x files/usr/bin/mihomo
chmod +x files/etc/mihomo/modify_uv.py
# chmod +rw files/etc/config/mosdns
chmod +rw files/etc/config/mihomo
