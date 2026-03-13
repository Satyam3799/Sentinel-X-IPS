# 🔱 Operation Rakta-beej: Dynamic IPS Engine
> **A behavior-based Intrusion Prevention System that neutralizes network attackers in real-time.**

Operation Rakta-beej is a next-gen security tool that monitors network reconnaissance attempts (like port scanning) and automatically orchestrates firewall rules to block threats. Inspired by the mythological legend where every drop of blood creates a new shield, this engine ensures that for every malicious probe, a new layer of defense is born.

---

## ✨ Features
- **Real-time Packet Inspection:** Uses Scapy to sniff and analyze incoming TCP traffic.
- **Behavioral Blocking:** Detects port scanning patterns and triggers an immediate OS-level block.
- **Cloud-Synced Dashboard:** Instantly pushes incident data to Supabase for global observability.
- **Live UI Visualization:** Real-time attack tracking via a modern Lovable-powered frontend.
- **Stealth Operation:** Runs as a lightweight background engine with minimal resource footprint.

---

## 📋 Prerequisites
Before you begin, ensure you have met the following requirements:
- **OS:** Windows 10/11 (with Administrative privileges)
- **Python:** Version 3.8 or higher
- **Npcap:** Required for raw packet sniffing — [Download here](https://nmap.org/npcap/)
- **Supabase Account:** To host the backend database

---

## ⚙️ Configuration
The system relies on environment variables for secure cloud connectivity. Create a `.env` file in the root directory:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_public_key
```

---

## 🚀 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/Satyam3799/Sentinel-X-IPS.git
cd Sentinel-X-IPS
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify Npcap:** Ensure Npcap is installed and running on your system.

---

## 💻 Usage

To start the IPS engine, you **must** run your terminal as an **Administrator** (required for firewall modifications).

```bash
# Start the monitoring and protection engine
python raktabeej.py
```

### What Happens When an Attack is Detected:

Once running, if an attacker tries to scan your machine using Nmap (`nmap -sT <your-ip>`), the engine will:

1. Detect the scan pattern.
2. Add a `netsh` firewall rule to block the attacker's IP.
3. Update the Supabase table with the attack details.
4. Refresh the Live Dashboard on Lovable.

---

## 📂 Project Structure

```text
Sentinel-X-IPS/
├── raktabeej.py         # Core IPS engine & packet sniffer
├── sentinel_brain.py    # Logic for database & cloud syncing
├── cleaner.py           # Script to reset firewall rules
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (Private — do not commit)
├── .gitignore           # Ensures sensitive files aren't uploaded
└── README.md            # Project documentation
```

---

## 🗺️ Roadmap

- [x] Phase 1: Port Scan Detection Logic
- [x] Phase 2: Dynamic Windows Firewall Integration
- [x] Phase 3: Supabase Cloud Connectivity
- [x] Phase 4: Lovable Live Dashboard Deployment
- [ ] Phase 5: Machine Learning-based anomaly detection
- [ ] Phase 6: Linux (iptables) compatibility

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

*Developed with 🔱 by [Satyam Singh](https://github.com/Satyam3799) — Computer Science & Engineering*
