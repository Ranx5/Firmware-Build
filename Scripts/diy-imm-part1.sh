#!/bin/bash
# Add a feed source
./scripts/feeds update -a
./scripts/feeds install -a
# grep -wblr firewall ./include/target.mk | xargs sed -i 's/\<firewall\>/firewall4/g'
