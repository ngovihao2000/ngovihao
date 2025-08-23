from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Lấy host/port từ docker-compose.yml (qua environment variables)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Kết nối Redis
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    # test lưu 1 biến vào redis
    r.set("welcome", "Xin chào từ Redis!")
    msg = r.get("welcome")
    return render_template("index.html", message=msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
