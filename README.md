<div align="center">

# ⛏️ Mining Farm Project

### Automated Cryptocurrency Mining Farm Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Latest-000000.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Latest-4479A1.svg)](https://www.mysql.com/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-0088CC.svg)](https://telegram.org/)

**Multi-Currency Mining • Real-Time Monitoring • Centralized Management**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

[العربية](README-ar.md) | [English](#-mining-farm-project)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Security](#-security)
- [Contributing](#-contributing)

---

## 🎯 Overview

**Mining Farm Project** is an automated cryptocurrency mining farm management system with multi-currency support, real-time monitoring, and centralized Flask API. Supports Monero, Epic Cash, QRL, and more.

### ✨ Why Mining Farm Project?

- ⛏️ **Multi-Currency Mining** - Support for multiple cryptocurrencies
- 📊 **Comprehensive Monitoring** - Track performance of all devices
- 🤖 **Telegram Bot** - Management and monitoring through Telegram
- 🖥️ **Centralized Server** - Unified management for all devices

---

## 🌟 Features

### 🚀 Main Features

| Feature | Description |
|---------|-------------|
| ⛏️ **Multi-Currency Mining** | Support for Monero, Epic Cash, QRL, and more |
| 📊 **Real-Time Monitoring** | Track mining device performance in real-time |
| 🤖 **Telegram Bot** | Management and monitoring through Telegram |
| 🖥️ **Centralized Server** | Central API for managing all mining devices |
| 📈 **Detailed Reports** | Detailed statistics and performance for each device |
| 🔄 **Automatic Management** | Automatic management of mining devices |

### 💰 Supported Currencies

- ✅ **Monero (XMR)** - CPU/GPU mining
- ✅ **Epic Cash** - CPU mining
- ✅ **QRL (Quantum Resistant Ledger)** - CPU mining
- ✅ **And more...**

---

## 📦 Requirements

Before starting, make sure you have installed:

- **Python** 3.8 or higher
- **MySQL** 5.7+ or 8.0+
- **Telegram Bot Token** (from [@BotFather](https://t.me/BotFather))
- **Mining Devices** (Miners) with XMRig or other mining software
- **Git**

---

## 🚀 Installation

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/3bkader-gpt/mining-farm-project.git
cd mining-farm-project

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Set up database
mysql -u root -p
CREATE DATABASE mining_farm;
```

### Database Setup

```sql
CREATE DATABASE mining_farm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'mining_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON mining_farm.* TO 'mining_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## ⚙️ Configuration

### `.env` File

Copy `.env.example` and create `.env` file:

```env
# Database
DB_HOST=localhost
DB_USER=mining_user
DB_PASSWORD=your_password
DB_NAME=mining_farm

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Server
SERVER_HOST=0.0.0.0
SERVER_PORT=5000

# Mining Settings
MINING_POOL_URL=pool.minexmr.com:443
MINING_WALLET_ADDRESS=your_wallet_address
```

### Telegram Bot Setup

1. Talk to [@BotFather](https://t.me/BotFather)
2. Create a new bot using `/newbot`
3. Get the Token
4. Add Token in `.env` file

### Mining Device Setup

1. Install `worker_script.py` on each mining device
2. Edit settings in script:
   ```python
   SERVER_URL = "http://your-server-ip:5000"
   WORKER_ID = "worker-1"  # Unique ID for each device
   ```
3. Run script on each device:
   ```bash
   python worker_script.py
   ```

---

## 📖 Usage

### Running Central Server

```bash
python central_server.py
```

Server will run on `http://localhost:5000`

### Running Telegram Bot

```bash
python telegram_bot.py
```

### API Endpoints

#### Get List of Devices

```bash
GET /api/workers
```

#### Get Device Information

```bash
GET /api/workers/{worker_id}
```

#### Get Statistics

```bash
GET /api/stats
```

### Telegram Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot |
| `/status` | Status of all devices |
| `/worker {id}` | Information about specific device |
| `/stats` | General statistics |
| `/start_mining` | Start mining on all devices |
| `/stop_mining` | Stop mining |
| `/restart {id}` | Restart specific device |

---

## 📁 Project Structure

```
mining-farm-project/
├── 📄 central_server.py     # Central server (API)
├── 📄 telegram_bot.py        # Telegram bot
├── 📄 worker_script.py      # Worker script (on mining devices)
├── 📄 .env.example          # Environment file example
└── 📄 requirements.txt      # Requirements
```

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Description |
|------------|-------------|
| ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white) | Main programming language |
| ![Flask](https://img.shields.io/badge/Flask-Latest-000000?logo=flask&logoColor=white) | Web framework |
| ![MySQL](https://img.shields.io/badge/MySQL-Latest-4479A1?logo=mysql&logoColor=white) | Database |
| ![Telegram](https://img.shields.io/badge/Telegram-Bot-0088CC?logo=telegram&logoColor=white) | Telegram bot |
| ![XMRig](https://img.shields.io/badge/XMRig-Miner-FF6B00?logo=xmrig&logoColor=white) | Mining software |

</div>

---

## 📊 Advanced Features

### Real-Time Monitoring

- 📈 Instant device status updates
- 📊 Detailed statistics for each device
- ⚡ Alerts when problems occur
- 📱 Telegram notifications

### Automatic Management

- 🔄 Automatic restart on failure
- ⚙️ Automatic settings adjustment
- 📊 Performance analysis and optimization
- 🔔 Smart alerts

---

## 🔒 Security

### Best Practices

- 🔐 **Protect Database** - Use strong passwords
- 🔒 **Use HTTPS** - For API in production
- 🛡️ **Secure Devices** - Secure mining devices
- 🔑 **Don't Share Keys** - Protect API keys

### Security Settings

```env
# Use HTTPS in production
USE_HTTPS=true
SSL_CERT_PATH=/path/to/cert.pem
SSL_KEY_PATH=/path/to/key.pem

# Enable authentication
ENABLE_AUTH=true
API_KEY=your_secure_api_key
```

---

## ⚠️ Important Warnings

### Before Starting

- ⚡ **Power Consumption** - Mining consumes a lot of electricity
- 💰 **Costs** - Make sure you understand electricity costs
- 🌡️ **Cooling** - Ensure proper cooling for devices
- ⚖️ **Laws** - Comply with local laws

### Important Tips

- 📊 Continuously monitor power consumption
- 🌡️ Monitor temperatures
- 💻 Use appropriate devices for mining
- 📈 Calculate profitability before starting

---

## 📄 License

This project is open source and available for free use.

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. 🍴 Fork the project
2. 🌿 Create a branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

---

## 📞 Contact & Support

- 🐛 **Report Issues**: [Open an Issue](https://github.com/3bkader-gpt/mining-farm-project/issues)
- 💡 **Suggest Features**: [Open an Issue](https://github.com/3bkader-gpt/mining-farm-project/issues)
- 📧 **Email**: medo.omar.salama@gmail.com

---

<div align="center">

**Made with ❤️ by [Mohamed Omar](https://github.com/3bkader-gpt)**

⭐ If you like this project, don't forget to give it a star!

⚠️ **Warning**: This project is for educational use. Make sure you understand the risks of cryptocurrency mining.

[⬆ Back to Top](#-mining-farm-project)

</div>