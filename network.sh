#!/bin/bash


param($1 , $2 , $3)

echo "auto eth0" |  sudo nano /etc/network/interfaces
echo "iface eth0 inet dhcp" |  sudo nano /etc/network/interfaces


echo "auto eth0" | sudo nano /etc/network/interfaces
echo "iface eth0" inet static | sudo nano /etc/network/interfaces
echo "address"+ $1 | sudo nano /etc/network/interfaces

echo "netmask " + $3 | sudo nano /etc/network/interfaces
echo "gateway"+ $2 | sudo nano /etc/network/interfaces 
echo  "dns-nameservers 4.4.4.4" | sudo nano /etc/network/interfaces 
echo  "dns-nameservers 8.8.8.8"| sudo nano /etc/network/interfaces

echo "static" >  conf.txt