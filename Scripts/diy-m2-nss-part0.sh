
#!/bin/bash
# 修改feeds.conf.default
sed -i 's/breeze303/Ranx5/g' feeds.conf.default
./scripts/feeds update -a
./scripts/feeds install -a
