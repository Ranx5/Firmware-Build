#!/bin/bash
local_version=$(mihomo -v | sed -n 's/.*\(v[0-9]\+\.[0-9]\+\.[0-9]\+\).*/\1/p')
echo "当前版本号：$local_version"
release_data=$(curl -s https://api.github.com/repos/MetaCubeX/mihomo/releases/latest)
# 获取仓库的最新发布信息
tag=$(echo "$release_data" | jq -r '.tag_name')
echo "最新版本号：$tag"
if [ "$local_version" != "$tag" ]; then
    echo "新版本可用，开始更新！"
    # 构建文件名
    target_name="mihomo-linux-arm64-$tag.gz"
    # 解析JSON以获取文件下载链接
    download_url=$(echo "$release_data" | jq -r --arg filename "$target_name" '.assets[] | select(.name == $filename) | .browser_download_url')
    # 下载文件
    if [ -n "$download_url" ]; then
        curl -L --retry 3 -o "$target_name" "$download_url"
        if [[ -f "$target_name" && $(stat --format="%s" "$target_name") -gt 0 ]]; then
            echo "下载成功: $target_name"
        else
            echo "$target_name下载失败，请检查网络！"
            exit 1
        fi
        gunzip $target_name
        chmod +x $target_name
        cp -f $target_name /usr/bin/mihomo
        service openclash stop
        mv $target_name /etc/openclash/core/clash_meta
        service openclash start
        echo "mihomo更新成功！"
    else
        echo "无法获取 $target_name的下载链接！"
    fi
else
    echo "已是最新版本: $local_version"
fi
