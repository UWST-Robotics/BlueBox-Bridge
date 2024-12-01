#!/bin/bash

systemctl unmask hostapd
systemctl enable hostapd

echo "interface wlan0
    static ip_address=192.168.1.1/24
    nohook wpa_supplicant" | sudo tee /etc/dhcpcd.conf.adhoc

    mv /etc/dhcpcd.conf /etc/dhcpcd.conf.wifi
    mv /etc/dhcpcd.conf.adhoc /etc/dhcpcd.conf


echo "# Enable IPv4 routing
net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/routed-ap.conf


iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
netfilter-persistent save
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig


echo "interface=wlan0 # Listening interface
dhcp-range=192.168.1.2,192.168.1.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/gw.wlan/192.168.1.1
                # Alias for this router" | sudo tee /etc/dnsmasq.conf


rfkill unblock wlan


echo "country_code=US
interface=wlan0
ssid=BlueBox
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=BlueBox
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP" | sudo tee /etc/hostapd/hostapd.conf