# BlueBox-Bridge




Helpful functions

    sudo netstat -lptu
    
    sudo systemctl status ser2net
    
    sudo systemctl restart ser2net



# Install Directions

## Install Operating System

Install Default Operating System via Rasberry Pi Imager (https://www.raspberrypi.com/software/)

Chose the correct device (Raspberry pi Zero 2 recommended)

Chose "Raspberry Pi OS LITE (64 bit)" as Operating System

Chose Correct storage device




## Install Services ( AS SUDO )

get services

    apt install git -y

    cd /home/bluebox

    git clone https://github.com/UWST-Robotics/BlueBox-Bridge.git

    chmod +x install.sh

    ./install.sh
        apt update
        apt upgrade -y
        apt-get install pip -y
        apt install python3-fastapi -y
        apt install ser2net -y
        apt install hostapd
        apt install dnsmasq
        DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent


## Configure Hosted Wifi - (https://www.stevemurch.com/setting-up-a-raspberry-pi-for-ad-hoc-networking-tech-note/2022/12)

    systemctl unmask hostapd

    systemctl enable hostapd

    nano /etc/dhcpcd.conf.adhoc

    "interface wlan0
        static ip_address=192.168.1.1/24
        nohook wpa_supplicant
    "

    #Change out dhcpcd.conf
    mv /etc/dhcpcd.conf /etc/dhcpcd.conf.wifi
    mv /etc/dhcpcd.conf.adhoc /etc/dhcpcd.conf

    nano /etc/sysctl.d/routed-ap.conf
    
    "# Enable IPv4 routing
    net.ipv4.ip_forward=1"

    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

    netfilter-persistent save

    mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
    nano /etc/dnsmasq.conf

    "
    interface=wlan0 # Listening interface
    dhcp-range=192.168.1.2,192.168.1.20,255.255.255.0,24h
                    # Pool of IP addresses served via DHCP
    domain=wlan     # Local wireless DNS domain
    address=/gw.wlan/192.168.1.1
                    # Alias for this router
    "

    rfkill unblock wlan

    nano /etc/hostapd/hostapd.conf

    "
    country_code=US
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
    rsn_pairwise=CCMP
    "