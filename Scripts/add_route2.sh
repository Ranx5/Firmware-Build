#!/bin/bash
# 定义文件名
FILE_NAME=$1
# 检查文件是否存在
if [ -f "$FILE_NAME" ]; then
    echo "正在从文件 $FILE_NAME 中提取 IPv4 地址段..."
    # 提取 IPv4 地址段
    IP_ADDRESSES=$(grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' "$FILE_NAME" | sort -u)
    
    if [ -z "$IP_ADDRESSES" ]; then
        echo "未找到任何有效的 IPv4 地址。"
        exit 1
    fi
    echo "提取到的 IPv4 地址段："
    echo "$IP_ADDRESSES"

    # 遍历每个 IP 地址并添加到 OpenWrt 的静态路由
    for IP in $IP_ADDRESSES; do
        echo "正在添加静态路由：$IP"
        uci add network route
        uci set network.@route[-1].target="$IP"
        uci set network.@route[-1].gateway="$2"    # 替换为实际网关
        uci set network.@route[-1].interface="lan"         # 替换为实际接口名称
    done
    # 保存并应用配置
    uci commit network
    echo "所有静态路由已添加并提交。"
    /etc/init.d/network restart
    echo "网络服务已重启。"
else
    echo "文件 $FILE_NAME 不存在，请检查文件路径。"
    exit 1
fi
