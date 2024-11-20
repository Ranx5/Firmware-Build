#!/bin/sh
. /usr/share/openclash/log.sh
. /lib/functions.sh

# This script is called by /etc/init.d/openclash
# Add your custom firewall rules here, they will be added after the end of the OpenClash iptables rules

LOG_OUT "Tip: Start Add Custom Firewall Rules..."
en_mode=$(uci -q get openclash.config.en_mode)
proxy_port=$(uci -q get openclash.config.proxy_port)

if [ "$en_mode" == "fake-ip" ]; then
  LOG_OUT "Limit route to only fake ips with proxy port $proxy_port"
  openclash_rule=$(nft -a list chain inet fw4 openclash | grep $proxy_port |awk 'END {print $NF}')
  nft delete rule inet fw4 openclash handle $openclash_rule
  openclash_o_rule=$(nft -a list chain inet fw4 openclash_output | grep $proxy_port |awk 'END {print $NF}')
  nft delete rule inet fw4 openclash_output handle $openclash_o_rule

  nft -a list set inet fw4 openclash_proxy_ip
  if [ $? -eq 0 ]; then
    LOG_OUT "delete openclash_proxy_ip setting"
    nft delete set inet fw4 openclash_proxy_ip
  fi
  nft -a list set inet fw4 china_ip_route
  if [ $? -eq 0 ]; then
    LOG_OUT "Add special proxy rules"
    nft add rule inet fw4 openclash ip protocol tcp ip daddr != @china_ip_route  counter redirect to :7892
    nft add rule inet fw4 openclash_output ip protocol tcp ip daddr != @china_ip_route counter redirect to :7892
    else
    LOG_OUT "china_ip_route is not exist. Skip add the rules"
  fi
fi
/etc/init.d/mosdns restart
exit 0
