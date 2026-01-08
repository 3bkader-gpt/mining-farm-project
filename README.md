<div align="center">

# ⛏️ Mining Farm Project

### <p align="center">
  <span style="color: #7E3ACE; font-size: 2.2em; font-weight: 700; letter-spacing: 2px; line-height: 1.6;">
    ⛏️ Automated Cryptocurrency Mining Farm<br/>
    🚀 Multi-Currency Support & Management<br/>
    📊 Real-time Monitoring & Analytics
  </span>
</p>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/3bkader-gpt/mining-farm-project)

---

</div>

## 🌟 Features

<div align="center">

### ✨ **Powerful & Efficient**

| 🎯 **Core Features** | 📊 **Management** | 🔧 **Advanced** |
|:---:|:---:|:---:|
| ⛏️ Multi-Currency Mining | 📈 Real-time Analytics | 🔐 Secure Configuration |
| 🚀 Automated Setup | 📱 Telegram Notifications | 🗄️ Database Management |
| 💰 Profitability Tracking | 🎨 Web Dashboard | 🔄 Auto-Updates |

</div>

### 🚀 **Key Highlights**

- ⛏️ **Multi-Currency Support** - Mine Monero, Epic Cash, QRL, Zephyr, and more
- 🎯 **Optimized Performance** - Configured for Intel Xeon E3-1275 v5
- 📊 **Real-time Monitoring** - Track hashrate, profits, and server status
- 🤖 **Telegram Integration** - Get instant notifications and farm summaries
- 🗄️ **Centralized Management** - Flask API with MySQL database
- 🔄 **Auto-Reporting** - Workers automatically report to central server
- 📈 **Profitability Calculator** - Compare different cryptocurrencies
- 🛠️ **Easy Setup** - Simple installation and configuration

---

## 📸 Supported Cryptocurrencies

<div align="center">

| Currency | Symbol | Algorithm | Profitability | Status |
|:--------:|:------:|:---------:|:-------------:|:------:|
| **Epic Cash** | EPIC | RandomX | 124-128% vs Monero | ✅ Recommended |
| **Monero** | XMR | RandomX | 100% (baseline) | ✅ Stable |
| **QRL** | QRL | RandomX | 103% vs Monero | ✅ Good |
| **Zephyr** | ZEPH | RandomX | 74-85% vs Monero | ⚠️ Lower |
| **Raptoreum** | RTM | GhostRider | 20-23% vs Monero | ⚠️ Low |

</div>

---

## 🏗️ Architecture

<div align="center">

```
┌─────────────────┐
│  Worker Script  │ → Mines cryptocurrency
│   (v2.0)        │ → Reports to central server
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Central Server  │ → Flask API + MySQL
│  (Flask API)    │ → Stores farm statistics
└────────┬────────┘
         │
         ├──────────────┐
         │              │
         ▼              ▼
┌─────────────────┐  ┌─────────────────┐
│  Web Dashboard   │  │  Telegram Bot    │
│  (Port 5001)    │  │   (Notifier)     │
│  Real-time UI   │  │  Real-time msgs  │
└─────────────────┘  └─────────────────┘
```

</div>

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Telegram Bot API](https://img.shields.io/badge/-Telegram%20Bot%20API-2CA5E0?style=flat-square&logo=telegram&logoColor=white)
![XMRig](https://img.shields.io/badge/-XMRig-FF6B00?style=flat-square&logo=xmrig&logoColor=white)

</div>

---

## 📦 Installation

### **Prerequisites**

```bash
# Make sure you have Python 3.8+ installed
python --version

# Install system dependencies (Linux)
sudo apt-get update
sudo apt-get install -y wget tar gcc make mysql-server
```

### **Quick Start**

```bash
# 1️⃣ Clone the repository
git clone https://github.com/3bkader-gpt/mining-farm-project.git
cd mining-farm-project

# 2️⃣ Install Python dependencies
pip install -r requirements.txt

# 3️⃣ Setup MySQL database
sudo mysql_secure_installation
# Create database (see Configuration section)

# 4️⃣ Configure environment variables
# Update central_server.py with your MySQL credentials
# Update telegram_bot.py with your bot token

# 5️⃣ Start central server
python central_server.py

# 6️⃣ Start worker script (on mining machines)
python worker_script.py
```

---

## ⚙️ Configuration

### **Database Setup**

```sql
CREATE DATABASE mining_farm;
CREATE USER 'mining_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON mining_farm.* TO 'mining_user'@'localhost';
FLUSH PRIVILEGES;
```

### **Central Server Configuration**

Edit `central_server.py`:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="mining_user",
    password="your_password",  # Use environment variables in production!
    database="mining_farm"
)
```

### **Telegram Bot Configuration**

Edit `telegram_bot.py`:

```python
TOKEN = "YOUR_BOT_TOKEN"  # Get from @BotFather
CHAT_ID = "YOUR_CHAT_ID"  # Get from @userinfobot
CENTRAL_SERVER_URL = "http://YOUR_SERVER_IP:5000"
```

### **Worker Script Configuration**

Edit `worker_script.py`:

```python
central_server_url = "http://YOUR_SERVER_IP:5000"
wallet_address = "YOUR_WALLET_ADDRESS"
```

---

## 🎮 Usage

### **Starting the Central Server**

```bash
python central_server.py
# Server runs on http://0.0.0.0:5002
```

### **Starting Worker Scripts**

On each mining machine:

```bash
python worker_script.py
# Automatically installs XMRig and starts mining
```

### **Telegram Bot Commands**

Send messages to your Telegram bot:
- `summary` - Get farm summary
- `details` - Get detailed server information

---

## 📁 Project Structure

```
mining-farm-project/
├── 📄 central_server.py      # Flask API server
├── 📄 worker_script.py        # Mining worker script
├── 📄 telegram_bot.py         # Telegram notification bot
├── 📄 requirements.txt        # Python dependencies
├── 📖 README.md              # This file
└── 📁 docs/                  # Additional documentation
    ├── SERVER_SETUP.md
    ├── DEPLOY_INSTRUCTIONS.md
    └── ...
```

---

## 📊 API Endpoints

### **Central Server API**

- `POST /add_or_update_server` - Add/update worker server
- `GET /get_servers` - Get all servers
- `GET /get_summary` - Get farm summary

### **Example Usage**

```bash
# Get farm summary
curl http://YOUR_SERVER:5002/get_summary

# Get all servers
curl http://YOUR_SERVER:5002/get_servers
```

---

## 💰 Profitability

Based on Intel Xeon E3-1275 v5 (4 cores / 8 threads @ 3.6 GHz):

| Currency | Hashrate | Daily Profit | Monthly Profit |
|:--------:|:--------:|:------------:|:--------------:|
| Epic Cash | 2,000 H/s | $0.51 - $0.85 | $15.30 - $25.50 |
| Monero | 2,000 H/s | $0.32 - $0.66 | $9.60 - $19.80 |
| QRL | 2,000 H/s | $0.30 - $0.64 | $9.00 - $19.20 |

**Note:** Profits vary based on network difficulty, coin price, electricity costs, and pool fees.

---

## 🔒 Security Recommendations

⚠️ **Important:** Before production deployment:

1. **Use Environment Variables:**
```bash
export MYSQL_PASSWORD="your_password"
export TELEGRAM_TOKEN="your_token"
export WALLET_ADDRESS="your_wallet"
```

2. **Never Commit Secrets:**
Add to `.gitignore`:
```
.env
*.log
config.local.json
```

3. **Update Code to Use Environment Variables:**
```python
import os
password = os.getenv('MYSQL_PASSWORD')
```

---

## 🛠️ Troubleshooting

### **Miner Not Starting**

```bash
# Check if miner is installed
ls -la xmrig/xmrig

# Check permissions
chmod +x xmrig/xmrig

# Check logs
tail -f worker_script.log
```

### **Connection Issues**

```bash
# Verify central server is running
curl http://YOUR_SERVER:5002/get_summary

# Check firewall
sudo ufw allow 5002
```

### **Low Hashrate**

```bash
# Check CPU usage
htop

# Verify CPU frequency
cat /proc/cpuinfo | grep MHz

# Check temperature
sensors
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

<div align="center">

### **Mohamed Omar**

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/3bkader-gpt)
[![Email](https://img.shields.io/badge/-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:medo.omar.salama@gmail.com)

---

### ⭐ **Star this repo if you find it helpful!**

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/3bkader-gpt/mining-farm-project?style=social)
![GitHub forks](https://img.shields.io/github/forks/3bkader-gpt/mining-farm-project?style=social)

---

**Made with ❤️ by [Mohamed Omar](https://github.com/3bkader-gpt)**

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=3bkader-gpt&color=blueviolet&style=flat-square" alt="Profile views" />
</p>

</div>

---

<div align="center">

### 🎉 **Thank you for visiting!**

<p align="center">
  <span style="color: #7E3ACE; font-size: 1.5em; font-weight: 600;">
    ⛏️ Happy Mining!<br/>
    🚀 Keep Building Amazing Things!
  </span>
</p>

</div>

---

<div align="center">

### ⚠️ **Disclaimer**

Cryptocurrency mining profitability varies. Always calculate electricity costs before mining. This project is for educational purposes.

**Credits:**
- **Miner:** [XMRig](https://github.com/xmrig/xmrig) - Open source miner
- **CPU Miner:** [cpuminer-opt](https://github.com/JayDDee/cpuminer-opt) - Multi-algorithm CPU miner

</div>
