from telegram import Bot
import requests

TOKEN = "7807067083:AAHHfP3WxJQUwaUrnbNI9e8tjbpKy0rY2G4"
CENTRAL_SERVER_URL = "http://192.168.1.15:5000"  # Central server IP
CHAT_ID = "6788399763"  # Telegram Chat ID

def get_farm_summary():
    response = requests.get(f"{CENTRAL_SERVER_URL}/get_summary")
    if response.status_code == 200:
        summary = response.json()
        message = f"Farm Summary:\n\n"
        message += f"Total Servers: {summary['total_servers']}\n"
        message += f"Active Servers: {summary['active_servers']}\n"
        message += f"Inactive Servers: {summary['inactive_servers']}\n"
        message += f"Total Hashrate: {summary['total_hashrate']} H/s\n"
        return message
    return "Failed to fetch farm summary."

def get_server_details():
    response = requests.get(f"{CENTRAL_SERVER_URL}/get_servers")
    if response.status_code == 200:
        servers = response.json()
        message = "Server Details:\n\n"
        for server in servers:
            message += f"Server: {server[1]}\nWallet: {server[2]}\nHashrate: {server[3]} H/s\nLast Update: {server[4]}\n\n"
        return message
    return "Failed to fetch server details."

def send_farm_status(command):
    bot = Bot(TOKEN)

    if command == "summary":
        message = get_farm_summary()
    elif command == "details":
        message = get_server_details()
    else:
        message = "Invalid command. Use 'summary' or 'details'."

    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    # Example: Send summary or details based on user input
    send_farm_status("summary")
