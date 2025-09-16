from flask import Flask

# Tạo app Flask
app = Flask(__name__)

# Định nghĩa route /api/ping
@app.route("/api/ping", methods=["GET"])
def ping():
    return {"message": "pong"}

# Chạy server
if __name__ == "__main__":
    app.run(debug=True)
