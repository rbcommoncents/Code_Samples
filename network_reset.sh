#!/usr/bin/env bash
# ----------------------------
# Linux Network Reset Script
# Author: SysAdmin Utility
# ----------------------------

echo "[+] Stopping networking-related services..."
sudo systemctl stop NetworkManager 2>/dev/null
sudo systemctl stop networking 2>/dev/null
sudo systemctl stop docker docker.socket 2>/dev/null
sudo systemctl stop systemd-networkd 2>/dev/null

echo "[+] Removing virtual interfaces (veth, br-, docker0, wg, tun)..."
for iface in $(ip -o link show | awk -F': ' '{print $2}' | grep -E '^(veth|br-|docker0|wg|tun)'); do
    echo "    -> Deleting $iface"
    sudo ip link delete "$iface" 2>/dev/null
done

echo "[+] Flushing all non-loopback interfaces..."
for iface in $(ip -o link show | awk -F': ' '{print $2}' | grep -v '^lo'); do
    sudo ip addr flush dev "$iface" 2>/dev/null
done

echo "[+] Restarting base interfaces..."
sudo ip link set lo up
for iface in $(ip -o link show | awk -F': ' '{print $2}' | grep -E '^(enp|eth|wlp)'); do
    echo "    -> Bringing up $iface"
    sudo ip link set "$iface" up 2>/dev/null
done

echo "[+] Restarting networking services..."
sudo systemctl start NetworkManager 2>/dev/null || true
sudo systemctl start networking 2>/dev/null || true
sudo systemctl restart systemd-resolved 2>/dev/null || true

echo "[+] Renewing DHCP leases..."
for iface in $(ip -o link show | awk -F': ' '{print $2}' | grep -E '^(enp|eth|wlp)'); do
    sudo dhclient -r "$iface" 2>/dev/null
    sudo dhclient "$iface" 2>/dev/null
done

echo "[✓] Network reset complete. Current interfaces:"
ip addr show | grep -E '^[0-9]+: |inet '
