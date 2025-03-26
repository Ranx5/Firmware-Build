#!/bin/bash
curl -C - -o ad.txt https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/Filters/AWAvenue-Ads-Rule-Dnsmasq.conf
#curl -C - -o ad.txt https://gcore.jsdelivr.net/gh/TG-Twilight/AWAvenue-Ads-Rule@main/Filters/AWAvenue-Ads-Rule-Dnsmasq.conf
if [ $? -eq 0 ]; then
    echo "Download ad.txt successfully!"
    sed -i '/address/!d' ad.txt
    echo "Modify ad.txt successfully!"
    if [ ! -e /etc/copy_dnsmasq.conf ]; then
        cp -f /etc/dnsmasq.conf /etc/copy_dnsmasq.conf
    else
        cp -f /etc/copy_dnsmasq.conf /etc/dnsmasq.conf
    fi
    cat ad.txt >> /etc/dnsmasq.conf
    echo "Modify dnsmasq.conf successfully!"
    /etc/init.d/dnsmasq restart
    echo "Restart dnsmasq..."
else
    echo "Download failed, please rerun the script!"
fi



