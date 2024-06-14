#!/bin/bash
# 修改默认IP
sed -i 's/192.168.1.1/192.168.32.1/g' package/base-files/files/bin/config_generate
# 正常编译补丁
# sed -i 's/TARGET_CFLAGS += -DHAVE_MAP_SYNC/TARGET_CFLAGS += -DHAVE_MAP_SYNC -D_LARGEFILE64_SOURCE/' feeds/packages/utils/xfsprogs/Makefile
# 启用Firewall4
#sed -i 's/+firewall/+uci-firewall/g' feeds/luci/applications/luci-app-firewall/Makefile
# 添加luci-app-mosdns
find ./ | grep Makefile | grep v2ray-geodata | xargs rm -f
find ./ | grep Makefile | grep mosdns | xargs rm -f
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
git clone https://github.com/sbwml/v2ray-geodata package/v2ray-geodata
# 添加luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-alist
# git clone --depth=1 https://github.com/sbwml/luci-app-alist -b master package/alist
# 添加luci-theme-argone
git clone --depth=1 https://github.com/kenzok78/luci-theme-argone.git -b main package/luci-theme-argone
git clone --depth=1 https://github.com/kenzok78/luci-app-argone-config.git -b main package/luci-app-argone-config
# 添加luci-app-ssr-plus
# git clone --depth=1 https://github.com/fw876/helloworld.git -b master package/helloworld
# 添加luci-app-watchcat-plus
sudo rm -rf feeds/packages/utils/watchcat
sudo mkdir watchcat
sudo chmod -R 777 watchcat
git clone --depth=1 https://github.com/openwrt/packages.git -b master watchcat
cp -rf watchcat/utils/watchcat feeds/packages/utils/watchcat
sudo rm -rf watchcat
git clone --depth=1 https://github.com/gngpp/luci-app-watchcat-plus.git -b main package/luci-app-watchcat-plus
