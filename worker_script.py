import os
import subprocess
import requests
import logging
from logging.handlers import RotatingFileHandler

# إعداد logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = 'worker_script.log'

# إنشاء logger
logger = logging.getLogger('WorkerScriptLogger')
logger.setLevel(logging.DEBUG)

# إعداد ملف log مع تدوير الملفات
file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

# طباعة الرسائل على الشاشة كمان
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


def get_server_name(central_server_url):
    try:
        response = requests.get(f"{central_server_url}/get_servers")
        response.raise_for_status()
        existing_servers = [server[1] for server in response.json()]

        # Generate unique server name
        i = 1
        while True:
            server_name = f"Farm {i}"
            if server_name not in existing_servers:
                logger.info(f"Generated new server name: {server_name}")
                return server_name
            i += 1
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching server names from central server: {e}")
        raise

def install_xmrig():
    try:
        if not os.path.exists("xmrig"):
            logger.info("XMRig not found, starting installation...")
            os.system("wget https://github.com/xmrig/xmrig/releases/download/v6.20.0/xmrig-6.20.0-linux-x64.tar.gz")
            os.system("tar -xvf xmrig-6.20.0-linux-x64.tar.gz")
            os.system("mv xmrig-6.20.0 xmrig")
            logger.info("XMRig installed successfully.")
        else:
            logger.info("XMRig is already installed.")
    except Exception as e:
        logger.error(f"Error during XMRig installation: {e}")
        raise

def start_mining(wallet_address, server_name, pool_url="57.129.39.84:443"):
    try:
        xmrig_path = "./xmrig/xmrig"
        logger.info("Starting mining...")
        subprocess.Popen([xmrig_path, "--url", pool_url, "--user", wallet_address, "--pass", server_name, "--tls"])
        logger.info(f"Mining started successfully for server: {server_name} on pool: {pool_url}")
    except Exception as e:
        logger.error(f"Error starting mining: {e}")
        raise

def report_to_central_server(central_server_url, wallet_address, server_name):
    try:
        # Simulating hashrate for testing purposes
        hashrate = 1000  # Replace with actual parsing of xmrig logs

        data = {
            "name": server_name,
            "wallet": wallet_address,
            "hashrate": hashrate
        }

        response = requests.post(f"{central_server_url}/add_or_update_server", json=data)
        response.raise_for_status()
        logger.info(f"Reported to central server successfully for server: {server_name}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error reporting to central server: {e}")
        raise

if __name__ == "__main__":
    central_server_url = "http://192.168.1.15:5000"  # Central server IP
    wallet_address = "44ajcjLRNMRTxMBfeV1ZnAZ96AbgVD5ux8EDc4Hs2DrMe4eLKxLAFWVcdJCJnFDMaoK6hoPGpcSKDGbDtZpczjkU87gd5RP"

    try:
        logger.info("Worker script started.")
        server_name = get_server_name(central_server_url)
        install_xmrig()
        start_mining(wallet_address, server_name)
        report_to_central_server(central_server_url, wallet_address, server_name)
        logger.info("Worker script completed successfully.")
    except Exception as e:
        logger.error(f"Worker script failed: {e}")
