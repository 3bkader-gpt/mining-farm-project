import os
import subprocess
import requests
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from environment variables
CENTRAL_SERVER_URL = os.getenv('CENTRAL_SERVER_URL', 'http://localhost:5002')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS', '')
POOL_URL = os.getenv('POOL_URL', '57.129.39.84:443')
XMRIG_VERSION = os.getenv('XMRIG_VERSION', '6.20.0')

# Validate required configuration
if not WALLET_ADDRESS:
    raise ValueError("WALLET_ADDRESS environment variable is required")

# Logging setup
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = 'worker_script.log'

# Create logger
logger = logging.getLogger('WorkerScriptLogger')
logger.setLevel(logging.DEBUG)

# File handler with rotation
file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


def get_server_name(central_server_url):
    """Get unique server name from central server"""
    try:
        response = requests.get(f"{central_server_url}/get_servers", timeout=10)
        response.raise_for_status()
        existing_servers = response.json()
        existing_names = [server.get('name', '') for server in existing_servers]

        # Generate unique server name
        i = 1
        while True:
            server_name = f"Farm {i}"
            if server_name not in existing_names:
                logger.info(f"✅ Generated new server name: {server_name}")
                return server_name
            i += 1
            if i > 1000:  # Safety limit
                raise ValueError("Too many servers, cannot generate unique name")
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error fetching server names from central server: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        raise


def install_xmrig():
    """Install XMRig miner if not already installed"""
    try:
        if not os.path.exists("xmrig"):
            logger.info("📦 XMRig not found, starting installation...")
            
            xmrig_url = f"https://github.com/xmrig/xmrig/releases/download/v{XMRIG_VERSION}/xmrig-{XMRIG_VERSION}-linux-x64.tar.gz"
            tar_file = f"xmrig-{XMRIG_VERSION}-linux-x64.tar.gz"
            
            # Download XMRig
            logger.info(f"⬇️  Downloading XMRig v{XMRIG_VERSION}...")
            download_cmd = f"wget {xmrig_url} -O {tar_file}"
            result = os.system(download_cmd)
            
            if result != 0:
                raise Exception(f"Failed to download XMRig. Exit code: {result}")
            
            # Extract XMRig
            logger.info("📂 Extracting XMRig...")
            extract_cmd = f"tar -xzf {tar_file}"
            result = os.system(extract_cmd)
            
            if result != 0:
                raise Exception(f"Failed to extract XMRig. Exit code: {result}")
            
            # Rename directory
            rename_cmd = f"mv xmrig-{XMRIG_VERSION} xmrig"
            result = os.system(rename_cmd)
            
            if result != 0:
                raise Exception(f"Failed to rename XMRig directory. Exit code: {result}")
            
            # Clean up tar file
            if os.path.exists(tar_file):
                os.remove(tar_file)
            
            # Make executable
            xmrig_path = "./xmrig/xmrig"
            if os.path.exists(xmrig_path):
                os.chmod(xmrig_path, 0o755)
            
            logger.info("✅ XMRig installed successfully.")
        else:
            logger.info("✅ XMRig is already installed.")
    except Exception as e:
        logger.error(f"❌ Error during XMRig installation: {e}")
        raise


def start_mining(wallet_address, server_name, pool_url=None):
    """Start XMRig mining process"""
    if pool_url is None:
        pool_url = POOL_URL
    
    try:
        xmrig_path = "./xmrig/xmrig"
        
        if not os.path.exists(xmrig_path):
            raise FileNotFoundError(f"XMRig not found at {xmrig_path}")
        
        logger.info(f"⛏️  Starting mining for server: {server_name}")
        logger.info(f"💰 Wallet: {wallet_address[:20]}...")
        logger.info(f"🏊 Pool: {pool_url}")
        
        # Start XMRig in background
        subprocess.Popen([
            xmrig_path,
            "--url", pool_url,
            "--user", wallet_address,
            "--pass", server_name,
            "--tls",
            "--donate-level", "1"
        ])
        
        logger.info(f"✅ Mining started successfully for server: {server_name}")
    except FileNotFoundError as e:
        logger.error(f"❌ {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Error starting mining: {e}")
        raise


def report_to_central_server(central_server_url, wallet_address, server_name):
    """Report server status to central server"""
    try:
        # TODO: Parse actual hashrate from XMRig logs
        # For now, using placeholder
        hashrate = 1000  # Replace with actual parsing of xmrig logs

        data = {
            "name": server_name,
            "wallet": wallet_address,
            "hashrate": hashrate,
            "currency": "XMR",
            "algorithm": "RandomX"
        }

        logger.info(f"📡 Reporting to central server: {central_server_url}")
        response = requests.post(
            f"{central_server_url}/add_or_update_server",
            json=data,
            timeout=10
        )
        response.raise_for_status()
        
        result = response.json()
        if result.get('status') == 'success':
            logger.info(f"✅ Reported to central server successfully for server: {server_name}")
        else:
            logger.warning(f"⚠️  Server reported but got unexpected response: {result}")
            
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error reporting to central server: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        raise


def main():
    """Main worker script function"""
    try:
        logger.info("🚀 Worker script started.")
        logger.info(f"📡 Central Server: {CENTRAL_SERVER_URL}")
        logger.info(f"💰 Wallet: {WALLET_ADDRESS[:20]}...")
        
        # Get unique server name
        server_name = get_server_name(CENTRAL_SERVER_URL)
        
        # Install XMRig if needed
        install_xmrig()
        
        # Start mining
        start_mining(WALLET_ADDRESS, server_name)
        
        # Report to central server
        report_to_central_server(CENTRAL_SERVER_URL, WALLET_ADDRESS, server_name)
        
        logger.info("✅ Worker script completed successfully.")
        logger.info("⛏️  Mining is running in the background.")
        
    except Exception as e:
        logger.error(f"❌ Worker script failed: {e}")
        raise


if __name__ == "__main__":
    main()
