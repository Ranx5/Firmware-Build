#!/bin/bash

# ANSI 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # 无色

# 用法检查
if [ $# -lt 2 ]; then
    echo -e "${RED}用法: $0 <下载地址> <User-Agent>${NC}"
    exit 1
fi

DOWNLOAD_URL="$1"
DOWNLOAD_UA="${2:-clash.meta}
DOWNLOAD_PATH="./config.yaml"  # 固定保存路径

echo -e "${GREEN}开始下载:${NC} $DOWNLOAD_URL"
echo -e "${GREEN}保存到:${NC} $DOWNLOAD_PATH"

# 执行curl下载并获取输出和HTTP状态码
# --progress-bar 单行进度条
CURL_OUTPUT=$(curl -w "\n%{http_code}" -SL \
  --progress-bar \
  --connect-timeout 30 \
  -m 60 \
  --speed-time 30 \
  --speed-limit 1 \
  --retry 2 \
  -H "User-Agent: ${DOWNLOAD_UA}" \
  "$DOWNLOAD_URL" \
  -o "$DOWNLOAD_PATH" 2>&1)

# 获取curl返回码和HTTP状态码
EXIR_CODE=${PIPESTATUS[0]}
HTTP_CODE=$(echo "$CURL_OUTPUT" | tail -n1)

# 判断下载结果
if [ "$EXIR_CODE" -ne 0 ] || [ "$HTTP_CODE" -ne 200 ]; then
    OUTPUT=$(echo "$CURL_OUTPUT" | sed '$d' | grep -a 'curl:' | tail -n 1)
    echo
    echo -e "【$DOWNLOAD_PATH】${RED}下载失败${NC}:【$OUTPUT】"
    rm -rf "$DOWNLOAD_PATH"
    exit 1
else
    echo
    echo -e "${GREEN}下载成功:${NC} $DOWNLOAD_PATH"
    exit 0
fi
