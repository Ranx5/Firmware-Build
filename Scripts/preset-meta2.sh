
#!/bin/bash

# 创建路径
mkdir -p files/etc/config
mkdir -p files/usr/bin
mkdir -p files/etc/openclash/core
mkdir -p files/etc/nikki/run

# 设置下载链接
GEOIP_URL="https://testingcf.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geoip.dat"
GEOSITE_URL="https://testingcf.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geosite.dat"
CLASH_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/openclash.config"
NIKKI_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Configs/nikki.config"
CONFIG_MODIFY_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/modify_uv.py"
NIKKI_MODIFY_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/main/Defconfig/mihomo_uv.py"
ANTI_ADS_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/main/Scripts/anti_ads.sh"
ADD_ROUTE_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/main/Scripts/add_route.sh"
DOWNLOAD_CONFIG_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/main/Scripts/download_config.sh"
# UPDATE_CORE_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/mainScripts/update_core.sh"

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
    echo "Mihomo complete!"
    wget -qO- "$download_url" | gunzip -c > files/etc/openclash/core/clash_meta
    echo "Openclash complete!"
else
    echo "Failed to retrieve download URL for $file_name."
fi

# 下载配置文件
wget -qO- $GEOIP_URL > files/etc/openclash/GeoIP.dat
wget -qO- $GEOSITE_URL > files/etc/openclash/GeoSite.dat
cp -f files/etc/openclash/Geo* files/etc/nikki/run
wget -qO- $CLASH_CONFIG_URL > files/etc/config/openclash
wget -qO- $NIKKI_CONFIG_URL > files/etc/config/nikki
wget -qO- $CONFIG_MODIFY_URL > files/etc/openclash/modify_uv.py
wget -qO- $NIKKI_MODIFY_URL > files/etc/nikki/mihomo_uv.py
wget -qO- $ANTI_ADS_URL > files/etc/openclash/anti_ads.sh
wget -qO- $ADD_ROUTE_URL > files/etc/openclash/add_route.sh
wget -qO- $DOWNLOAD_CONFIG_URL > files/etc/nikki/download_config.sh
# wget -qO- $UPDATE_CORE_URL > files/etc/openclash/update_core.sh

# 设置权限
chmod +x files/usr/bin/mihomo
chmod +x files/etc/openclash/anti_ads.sh
chmod +x files/etc/openclash/add_route.sh
# chmod +x files/etc/openclash/update_core.sh
chmod +x files/etc/openclash/core/clash*
chmod +x files/etc/openclash/modify_uv.py
chmod +x files/etc/nikki/mihomo_uv.py
chmod +x files/etc/nikki/download_config.sh
chmod +rw files/etc/config/openclash
chmod +rw files/etc/config/nikki
