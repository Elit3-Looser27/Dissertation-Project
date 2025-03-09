import requests
import json
import time

# ONOS API credentials
ONOS_BASE_URL = "http://localhost:8181/onos/v1/flows"
ONOS_AUTH = ("onos", "easy")

# Load trained ML model
loaded_model = tf.keras.models.load_model('ml_intrusion_detection_model.h5')

def fetch_network_data():
    """Simulated function to fetch network features for real-time detection"""
    # Fetched live network data (e.g., packet size, duration, source IP features)
    return np.random.rand(1, X_train.shape[1])  # Randomized for demonstration

def detect_and_mitigate():
    while True:
        # Fetch new data
        new_data = fetch_network_data()
        new_data = scaler.transform(new_data)
        
        # Predict anomaly
        prediction = loaded_model.predict(new_data)
        
        if prediction > 0.5:
            print("[ALERT] Anomaly detected! Triggering mitigation...")
            # Block suspicious traffic in ONOS
            block_malicious_traffic()
        else:
            print("[INFO] No anomalies detected.")
        
        time.sleep(5)  # Check every 5 seconds

def block_malicious_traffic():
    """Send a request to ONOS to block malicious traffic."""
    flow_rule = {
        "priority": 500,
        "isPermanent": True,
        "treatment": {"instructions": []},
        "selector": {"criteria": [{"type": "IPV4_SRC", "ip": "10.0.0.5/32"}]}
    }
    response = requests.post(ONOS_BASE_URL, auth=ONOS_AUTH, headers={"Content-Type": "application/json"}, data=json.dumps(flow_rule))
    print("[INFO] Flow rule added to ONOS:", response.status_code)

# Start detection and mitigation
detect_and_mitigate()