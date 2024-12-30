import os
import subprocess
import requests
import platform
import socket
import json

def get_server_name(central_server_url):
    response = requests.get(f"{central_server_url}/get_servers")
    existing_servers = [server[1] for server in response.json()]

    # Generate unique server name
    i = 1
    while True:
        server_name = f"Farm {i}"
        if server_name not in existing_servers:
            return server_name
        i += 1

def install_xmrig():
    # Check if XMRig exists
    if not os.path.exists("xmrig"):  # Assuming xmrig is extracted here
        os.system("wget https://github.com/xmrig/xmrig/releases/download/v6.20.0/xmrig-6.20.0-linux-x64.tar.gz")
        os.system("tar -xvf xmrig-6.20.0-linux-x64.tar.gz")
        os.system("mv xmrig-6.20.0 xmrig")


def start_mining(wallet_address, server_name, pool_url="57.129.39.84:443"):
    xmrig_path = "./xmrig/xmrig"
    
    # Start XMRig mining in background
    subprocess.Popen([xmrig_path, "--url", pool_url, "--user", wallet_address, "--pass", server_name, "--tls"])

def report_to_central_server(central_server_url, wallet_address, server_name):
    # Simulating hashrate for testing purposes
    hashrate = 1000  # Replace with actual parsing of xmrig logs

    data = {
        "name": server_name,
        "wallet": wallet_address,
        "hashrate": hashrate
    }

    response = requests.post(f"{central_server_url}/add_or_update_server", json=data)
    if response.status_code == 200:
        print("Reported to central server successfully.")
    else:
        print("Failed to report to central server.")

if __name__ == "__main__":
    central_server_url = "http://192.168.1.15:5000"  # Central server IP
    wallet_address = "44ajcjLRNMRTxMBfeV1ZnAZ96AbgVD5ux8EDc4Hs2DrMe4eLKxLAFWVcdJCJnFDMaoK6hoPGpcSKDGbDtZpczjkU87gd5RP"

    server_name = get_server_name(central_server_url)
    install_xmrig()
    start_mining(wallet_address, server_name)
    report_to_central_server(central_server_url, wallet_address, server_name)