from scapy.all import rdpcap, IP, TCP
import numpy as np

def process_pcap(pcap_file):
    """Extract network features from Wireshark PCAP files."""
    packets = rdpcap(pcap_file)
    features = []
    labels = []
    
    for pkt in packets:
        if IP in pkt and TCP in pkt:
            features.append([
                len(pkt),  # Packet size
                pkt[IP].ttl,  # Time-to-live value
                pkt[TCP].sport,  # Source port
                pkt[TCP].dport  # Destination port
            ])
            # Assume label 1 for attack traffic, 0 for normal
            labels.append(1 if pkt[TCP].dport == 80 else 0)
    
    return np.array(features), np.array(labels)

# Process a sample pcap file
features, labels = process_pcap('network_traffic.pcap')
np.save('network_data.npy', features)
np.save('network_labels.npy', labels)
print("[INFO] PCAP data processed and saved.")