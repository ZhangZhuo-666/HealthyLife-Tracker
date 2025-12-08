from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "HealthyLife Tracker is running"}

if __name__ == "__main__":
    app.run(debug=True)
