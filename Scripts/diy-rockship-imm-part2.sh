#!/bin/bash
# 添加luci-app-mosdns
rm -rf feeds/packages/net/mosdns
git clone https://github.com/sbwml/luci-app-mosdns -b v5 package/mosdns
# 添加luci-app-openclash
rm -rf feeds/luci/applications/luci-app-openclash
git clone --depth=1 https://github.com/vernesong/OpenClash.git -b dev package/luci-app-openclash
# 添加luci-app-nikki
git clone --depth=1 https://github.com/nikkinikki-org/OpenWrt-nikki.git -b main package/luci-app-nikki
# 更改Rust
mkdir rust
git clone https://github.com/immortalwrt/packages.git -b master rust
cd rust
git checkout 10862df850ae012b34ec9c57a9005b1f7e1e2aca
cd ..
rm -rf feeds/packages/lang/rust
cp -rf rust/lang/rust feeds/packages/lang/rust
rm -rf rust
