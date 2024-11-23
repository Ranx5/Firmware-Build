#!/bin/bash
curl -o ad.txt https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/refs/heads/main/Filters/AWAvenue-Ads-Rule-hosts.txtif [ $? -eq 0 ]; then
    echo "Download ad.txt successfully!"
fi
sed -i '/127/!d' ad.txt
sed -i '1d' ad.txt
sed -i 's/$/\//' ad.txt
sed -i 's/127.0.0.1 /address=\//' ad.txt
echo "Modify ad.txt successfully!"
if [ ! -e /etc/dnsmasq_copy.conf ]; then
    cp -f /etc/dnsmasq.conf /etc/dnsmasq_copy.conf
fi
cp -f /etc/dnsmasq_copy.conf /etc/dnsmasq.conf
cat ad.txt >> /etc/dnsmasq.conf
echo "Modify dnsmasq.conf successfully!"
/etc/init.d/dnsmasq restart
echo "Restart dnsmasq..."
