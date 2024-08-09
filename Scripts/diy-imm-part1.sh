#!/bin/bash
# 修改默认IP
sed -i 's/192.168.1.1/192.168.32.10/g' package/base-files/files/bin/config_generate
# 更新feed
./scripts/feeds update -a
./scripts/feeds install -a
# grep -wblr firewall ./include/target.mk | xargs sed -i 's/\<firewall\>/firewall4/g'
