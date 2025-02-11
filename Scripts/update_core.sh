#!/bin/bash
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
    wget -qO- "$download_url" | gunzip -c > /tmp/clash_meta
    chmod +x clash_meta
    service openclash stop
    mv /tmp/clash_meta /etc/openclash/core/clash_meta
    service openclash start
    echo "Update mihomo successfully！"
else
    echo "Failed to retrieve download URL for $file_name."
fi
