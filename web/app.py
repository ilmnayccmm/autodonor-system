from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    r = requests.get(f"{API_URL}/requests/all")
    data = r.json()
    return render_template("dashboard.html", requests=data)

if __name__ == "__main__":
    app.run(debug=True)
