from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

# الاتصال بقاعدة البيانات
conn = mysql.connector.connect(
    host="192.168.1.15",  # IP السيرفر المركزي
    user="root",  # اسم المستخدم
    password="Monero@2025#1234",  # كلمة المرور
    database="mining_farm"  # اسم قاعدة البيانات
)
cursor = conn.cursor()

# إنشاء جدول لو مش موجود
cursor.execute('''CREATE TABLE IF NOT EXISTS servers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) UNIQUE,
                    wallet VARCHAR(255),
                    hashrate INT,
                    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

@app.route('/add_or_update_server', methods=['POST'])
def add_or_update_server():
    data = request.json
    name = data['name']
    wallet = data['wallet']
    hashrate = data['hashrate']
    timestamp = datetime.datetime.now()

    try:
        # التحقق من وجود السيرفر
        cursor.execute("SELECT * FROM servers WHERE name = %s", (name,))
        existing_server = cursor.fetchone()

        if existing_server:
            # تحديث السيرفر
            cursor.execute("UPDATE servers SET wallet = %s, hashrate = %s, last_update = %s WHERE name = %s",
                           (wallet, hashrate, timestamp, name))
        else:
            # إضافة سيرفر جديد
            cursor.execute("INSERT INTO servers (name, wallet, hashrate, last_update) VALUES (%s, %s, %s, %s)",
                           (name, wallet, hashrate, timestamp))

        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get_servers', methods=['GET'])
def get_servers():
    cursor.execute("SELECT * FROM servers")
    servers = cursor.fetchall()
    return jsonify(servers)

@app.route('/get_summary', methods=['GET'])
def get_summary():
    cursor.execute("SELECT COUNT(*), SUM(hashrate) FROM servers")
    total_servers, total_hashrate = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM servers WHERE TIMESTAMPDIFF(MINUTE, last_update, NOW()) <= 5")
    active_servers = cursor.fetchone()[0]

    summary = {
        "total_servers": total_servers,
        "total_hashrate": total_hashrate,
        "active_servers": active_servers,
        "inactive_servers": total_servers - active_servers
    }
    return jsonify(summary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
