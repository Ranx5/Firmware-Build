#!/bin/sh
. /usr/share/openclash/log.sh
. /lib/functions.sh

# This script is called by /etc/init.d/openclash
# Add your custom firewall rules here, they will be added after the end of the OpenClash iptables rules

LOG_OUT "Tip: Start Add Custom Firewall Rules..."
curl -s https://anti-ad.net/anti-ad-for-dnsmasq.conf -o /etc/openclash/dnsmasq.d/anti-ad-for-dnsmasq.conf
/etc/init.d/dnsmasq restart
exit 0
