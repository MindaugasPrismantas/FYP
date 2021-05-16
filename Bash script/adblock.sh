#!/bin/sh
#clone this to /etc/adblock.sh


##### CONFIG START #####

set -e 

opkg update && opkg upgrade
opkg install adblock libustream-mbedtls
opkg install luci-app-adblock
# DNS block tracking
opkg install tcpdump-mini

echo "config interface 'loopback' /
		option ifname 'lo' /
		option proto 'static' /
		option ipaddr '127.0.0.1' /
		option netmask '255.0.0.0' /
		
	config globals 'globals' /
		option ula_prefix 'fd00:a121:35a3::/48' /
		
	config interface 'lan' /
		option type 'bridge' /
		option ifname 'eth0' /
		option proto 'static' /
		option netmask '255.255.255.0' /
		option ip6assign '60' /
		option ipaddr '192.168.0.2' /
		option gateway '192.168.0.1' /
		list dns '192.168.0.1' " >> /etc/config/network
		
uci set adblock.global.adb_backupdir="/etc/adblock"

uci commit adblock
/etc/init.d/adblock restart