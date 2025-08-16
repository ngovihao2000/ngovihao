from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    count = r.incr('visits')
    return f"hello thay oi em lam xong ori nhe"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
