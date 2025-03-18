from scapy.all import rdpcap, IP, TCP
import numpy as np

def process_pcap(pcap_file):
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
            labels.append(1 if pkt[TCP].dport == 80 else 0)  # 1 for attack, 0 for normal
    
    return np.array(features), np.array(labels)

features, labels = process_pcap('network_traffic.pcap')
np.save('network_data.npy', features)
np.save('network_labels.npy', labels)