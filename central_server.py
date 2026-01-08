from flask import Flask, request, jsonify
import mysql.connector
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database configuration from environment variables
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'mining_farm')
DB_PORT = int(os.getenv('DB_PORT', 3306))

# Server configuration
SERVER_PORT = int(os.getenv('SERVER_PORT', 5002))
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')

# Connection to database
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
        autocommit=False
    )
    cursor = conn.cursor()
    print(f"✅ Successfully connected to MySQL database: {DB_NAME}")
except mysql.connector.Error as e:
    print(f"❌ Error connecting to MySQL: {e}")
    raise

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS servers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) UNIQUE,
                    wallet VARCHAR(255),
                    hashrate INT,
                    currency VARCHAR(10) DEFAULT 'XMR',
                    algorithm VARCHAR(50) DEFAULT 'RandomX',
                    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)''')
conn.commit()

# Enable CORS for dashboard
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        cursor.execute("SELECT 1")
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route('/add_or_update_server', methods=['POST'])
def add_or_update_server():
    """Add or update server information"""
    data = request.json
    
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    
    name = data.get('name')
    wallet = data.get('wallet')
    hashrate = data.get('hashrate')
    currency = data.get('currency', 'XMR')
    algorithm = data.get('algorithm', 'RandomX')
    timestamp = datetime.datetime.now()

    if not name or not wallet:
        return jsonify({"status": "error", "message": "Name and wallet are required"}), 400

    try:
        # Check if server exists
        cursor.execute("SELECT * FROM servers WHERE name = %s", (name,))
        existing_server = cursor.fetchone()

        if existing_server:
            # Update server
            cursor.execute("""
                UPDATE servers 
                SET wallet = %s, hashrate = %s, currency = %s, algorithm = %s, last_update = %s 
                WHERE name = %s
            """, (wallet, hashrate, currency, algorithm, timestamp, name))
            message = "Server updated successfully"
        else:
            # Add new server
            cursor.execute("""
                INSERT INTO servers (name, wallet, hashrate, currency, algorithm, last_update) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, wallet, hashrate, currency, algorithm, timestamp))
            message = "Server added successfully"

        conn.commit()
        return jsonify({"status": "success", "message": message}), 200
    except mysql.connector.Error as e:
        conn.rollback()
        return jsonify({"status": "error", "message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        conn.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_servers', methods=['GET'])
def get_servers():
    """Get all servers"""
    try:
        cursor.execute("SELECT * FROM servers ORDER BY last_update DESC")
        servers = cursor.fetchall()
        
        # Convert to list of dictionaries
        result = []
        for server in servers:
            result.append({
                "id": server[0],
                "name": server[1],
                "wallet": server[2],
                "hashrate": server[3],
                "currency": server[4] if len(server) > 4 else "XMR",
                "algorithm": server[5] if len(server) > 5 else "RandomX",
                "last_update": server[6].isoformat() if server[6] else None
            })
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_summary', methods=['GET'])
def get_summary():
    """Get farm summary statistics"""
    try:
        cursor.execute("SELECT COUNT(*), SUM(hashrate) FROM servers")
        total_servers, total_hashrate = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) FROM servers WHERE TIMESTAMPDIFF(MINUTE, last_update, NOW()) <= 5")
        active_servers = cursor.fetchone()[0]

        summary = {
            "total_servers": total_servers or 0,
            "total_hashrate": total_hashrate or 0,
            "active_servers": active_servers or 0,
            "inactive_servers": (total_servers or 0) - active_servers
        }
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    import sys
    import socket
    
    # Try configured port first
    port = SERVER_PORT
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    # Check if port is available
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    
    if result == 0:
        print(f"⚠️  Port {port} is already in use, trying {port + 1}...")
        port = port + 1
    
    print(f"🚀 Starting Central Server on {SERVER_HOST}:{port}...")
    print(f"📊 Database: {DB_NAME} @ {DB_HOST}:{DB_PORT}")
    app.run(host=SERVER_HOST, port=port, debug=False)
