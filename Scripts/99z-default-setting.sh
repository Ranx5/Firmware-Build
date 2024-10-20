#!/bin/bash
uci add_list dhcp.@dnsmasq[0].addnhosts='/etc/openclash/anti-ad-for-dnsmasq.conf'
uci commit dhcp
/etc/init.d/dnsmasq restart
uci set openclash.config.dashboard_password='123456'
uci commit openclash
