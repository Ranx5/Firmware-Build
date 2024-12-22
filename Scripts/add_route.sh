#!/bin/bash
DEFAULT_GATEWAY="192.168.32.11"
DEFAULT_URL="https://raw.githubusercontent.com/Ranx5/Firmware-Build/refs/heads/main/Defconfig/route.txt"
# 网关地址从第一个参数获取
gateway=${1:-$DEFAULT_GATEWAY}
url=${2:-$DEFAULT_URL}
# 拉取远程文件
curl -s $url | \
{
    # 判断 curl 是否拉取成功
    if [ $? -eq 0 ]; then
        echo "Curl 拉取成功，开始处理 IP 地址段..."
        # 过滤出符合 IPv4 地址段的行
        grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[0-9]+' | \
        while read ip_range; do
            # 提取目标 IP 段（CIDR 格式）和网关
            target=$ip_range  # CIDR 地址（整个 IP 地址段）
            # 添加路由规则
            uci add network route
            uci set network.@route[-1].interface='lan'  # 替换为实际接口名
            uci set network.@route[-1].target=$target
            uci set network.@route[-1].gateway=$gateway
        done
        # 提交并重启网络服务
        uci commit network
        /etc/init.d/network restart
        echo "路由规则已成功添加并生效。"
    else
        echo "Curl 拉取文件失败，请检查 URL 或网络连接。"
        exit 1
    fi
}
