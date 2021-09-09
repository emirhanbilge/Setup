#!/bin/bash


#param($1 , $2 , $3)

echo 1234 | sudo -S su


echo "auto eth0" >>  /etc/network/interfaces
echo "iface eth0 inet dhcp" >>  /etc/network/interfaces


echo "auto eth0" >>   /etc/network/interfaces
echo "iface eth0" >> /etc/network/interfaces
echo "inet static" >>  /etc/network/interfaces
echo "address {$1}"  >>  /etc/network/interfaces

echo "ip address" 
echo $1

echo "gateway"
echo $2

echo "netmask"
echo $3


echo "" >   /etc/network/interfaces
echo "netmask {$3} "  >>   /etc/network/interfaces
echo "gateway {$2}"  >>   /etc/network/interfaces 
echo  "dns-nameservers 4.4.4.4" >>  /etc/network/interfaces 
echo  "dns-nameservers 8.8.8.8" >>  /etc/network/interfaces

echo "static" >  conf.txt
