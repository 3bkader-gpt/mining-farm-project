from telegram import Bot
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
CENTRAL_SERVER_URL = os.getenv('CENTRAL_SERVER_URL', 'http://localhost:5002')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

# Validate required configuration
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
if not CHAT_ID:
    raise ValueError("TELEGRAM_CHAT_ID environment variable is required")

def get_farm_summary():
    """Get farm summary from central server"""
    try:
        response = requests.get(f"{CENTRAL_SERVER_URL}/get_summary", timeout=10)
        response.raise_for_status()
        summary = response.json()
        
        message = "📊 **Farm Summary**\n\n"
        message += f"🖥️  Total Servers: {summary.get('total_servers', 0)}\n"
        message += f"✅ Active Servers: {summary.get('active_servers', 0)}\n"
        message += f"❌ Inactive Servers: {summary.get('inactive_servers', 0)}\n"
        message += f"⚡ Total Hashrate: {summary.get('total_hashrate', 0):,} H/s\n"
        
        return message
    except requests.exceptions.RequestException as e:
        return f"❌ Failed to fetch farm summary: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_server_details():
    """Get detailed server information"""
    try:
        response = requests.get(f"{CENTRAL_SERVER_URL}/get_servers", timeout=10)
        response.raise_for_status()
        servers = response.json()
        
        if not servers:
            return "📋 No servers found."
        
        message = "📋 **Server Details**\n\n"
        for server in servers:
            message += f"🖥️  **{server.get('name', 'Unknown')}**\n"
            message += f"💰 Wallet: `{server.get('wallet', 'N/A')[:20]}...`\n"
            message += f"⚡ Hashrate: {server.get('hashrate', 0):,} H/s\n"
            message += f"🪙 Currency: {server.get('currency', 'XMR')}\n"
            message += f"🔧 Algorithm: {server.get('algorithm', 'RandomX')}\n"
            message += f"🕐 Last Update: {server.get('last_update', 'N/A')}\n\n"
        
        return message
    except requests.exceptions.RequestException as e:
        return f"❌ Failed to fetch server details: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def send_farm_status(command):
    """Send farm status to Telegram"""
    try:
        bot = Bot(TOKEN)

        if command == "summary":
            message = get_farm_summary()
        elif command == "details":
            message = get_server_details()
        else:
            message = "❌ Invalid command. Use 'summary' or 'details'."

        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
        print(f"✅ Message sent successfully: {command}")
    except Exception as e:
        print(f"❌ Error sending message: {str(e)}")

if __name__ == "__main__":
    import sys
    
    # Get command from command line argument or use default
    command = sys.argv[1] if len(sys.argv) > 1 else "summary"
    
    print(f"🤖 Telegram Bot started")
    print(f"📡 Central Server: {CENTRAL_SERVER_URL}")
    print(f"💬 Sending {command}...")
    
    send_farm_status(command)
