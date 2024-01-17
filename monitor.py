from scapy.all import sniff, ARP, IP, TCP, UDP
import random

def random_mask_address(addr, is_mac=False):
        if is_mac:
            masked_mac = "20:3D:6^:AE:3A:B1"
            return masked_mac
        else:
            masked_ip = "12.187.12.222"
            return masked_ip
        
def packet_callback(packet):
    if ARP in packet and packet[ARP].op in (1, 2):  # ARP request (1) or reply (2)
        masked_src_ip = random_mask_address(packet[ARP].psrc)
        masked_src_mac = random_mask_address(packet[ARP].hwsrc, is_mac=True)
        print(f"ARP {['who-has', 'is-at'][packet[ARP].op-1]} {masked_src_ip} ({masked_src_mac})")
    elif IP in packet:
        masked_src_ip = random_mask_address(packet[IP].src)
        masked_dst_ip = random_mask_address(packet[IP].dst)
        print(f"IP {masked_src_ip} -> {masked_dst_ip}")
        if TCP in packet:  # Any TCP traffic
            print(f"TCP {masked_src_ip}:{packet[TCP].sport} -> {masked_dst_ip}:{packet[TCP].dport}")
        elif UDP in packet:  # Any UDP traffic
            print(f"UDP {masked_src_ip}:{packet[UDP].sport} -> {masked_dst_ip}:{packet[UDP].dport}")

# Adjust the interface parameter based on your network interface
interface = ""  # Replace with your monitor mode interface

print(f"Monitoring ARP, IP, TCP, UDP traffic on interface {interface}...")

# Start sniffing packets on the specified interface
sniff(prn=packet_callback, filter="(arp or ip or tcp or udp)", store=0, iface=interface)