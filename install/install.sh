#!/bin/bash
apt update
apt upgrade -y
apt-get install pip -y
apt install python3-fastapi -y
apt install ser2net -y
apt install hostapd
apt install dnsmasq
DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent
# configure execute permissions
chmod +x BlueBox-Bridge/sh/run.sh
chmod +x BlueBox-Bridge/sh/ap_mode.sh
chmod +x BlueBox-Bridge/sh/wifi.sh
chmod +x BlueBox-Bridge/install/config.sh
