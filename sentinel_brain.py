import os
from scapy.all import sniff, IP, TCP
from supabase import create_client
from collections import defaultdict

# --- RAKTA-BEEJ CLOUD CONFIG ---
URL = "https://irxrhxyyzajpatwfsoud.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlyeHJoeHl5emFqcGF0d2Zzb3VkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMzNzIwMTcsImV4cCI6MjA4ODk0ODAxN30.qu6up56J7LkAKHKgi7YR4PTUTJl8ZWVHwy_OBbG66DY"

supabase = create_client(URL, KEY)

# Threshold: 10 unique ports hit hote hi Rakta-beej active ho jayega
port_tracker = defaultdict(set)
THRESHOLD = 10 

def report_to_dashboard(ip, port_count):
    try:
        data = {
            "attacker_ip": ip, 
            "attack_type": f"RAKTA-BEEJ: Port Scan Detected ({port_count} ports)", 
            "severity": "CRITICAL", 
            "action_taken": "IP Neutralized via OS-Level Firewall"
        }
        supabase.table("attacks").insert(data).execute()
        print(f"🚀 [RAKTA-BEEJ] Incident Synced to Cloud for IP: {ip}")
    except Exception as e:
        print(f"❌ Cloud Sync Error: {e}")

def block_hacker(ip):
    # Creating a dynamic firewall rule
    rule_name = f"RaktaBeej_Block_{ip.replace('.', '_')}"
    # Pehle purana rule delete karenge (if exists) taaki duplicate na ho
    os.system(f"netsh advfirewall firewall delete rule name='{rule_name}' >nul 2>&1")
    # Naya block rule add karenge
    os.system(f"netsh advfirewall firewall add rule name='{rule_name}' dir=in action=block remoteip={ip}")
    print(f"⛔ Firewall: [RAKTA-BEEJ] Neutralized attacker at {ip}")

def monitor_traffic(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        src_ip = pkt[IP].src
        dport = pkt[TCP].dport
        
        # Unique port tracking logic
        port_tracker[src_ip].add(dport)
        current_count = len(port_tracker[src_ip])
        
        # Agar threshold cross hua toh surgical strike
        if current_count > THRESHOLD:
            print(f"⚠️  RAKTA-BEEJ ALERT: {src_ip} hit {current_count} ports! Initiating Counter-Measure...")
            block_hacker(src_ip)
            report_to_dashboard(src_ip, current_count)
            port_tracker[src_ip].clear() # Reset for next wave

# --- STARTING THE ENGINE ---
print("🔱 OPERATION RAKTA-BEEJ: ACTIVE")
print("🛡️  Status: Monitoring Network for Reconnaissance...")
print("📡  Zero-Input Engine Running. No escape for attackers.")
print("-" * 50)

try:
    # Filter: tcp packets capture karo
    sniff(filter="tcp", prn=monitor_traffic, store=0)
except Exception as e:
    print(f"❌ FATAL ERROR: {e}")
    print("TIP: Run as Administrator and ensure Npcap is installed.")

input("\nPress Enter to close the engine...")