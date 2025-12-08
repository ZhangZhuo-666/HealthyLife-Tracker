from flask import Flask, request, jsonify
from models import HealthRecord
from storage import load_data, save_data

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "HealthyLife Tracker is running"}


@app.post("/add")
def add_record():
    data = request.json

    record = HealthRecord(
        date=data["date"],
        activity=data["activity"],
        duration=data["duration"],
        water_intake=data["water_intake"],
        sleep_hours=data["sleep_hours"]
    )

    records = load_data()
    records.append(record.__dict__)
    save_data(records)

    return jsonify({"status": "success", "message": "Record added!"})


@app.get("/records")
def get_records():
    records = load_data()
    return jsonify(records)


@app.get("/weekly-summary")
def weekly_summary():
    records = load_data()

    if not records:
        return jsonify({"message": "No records found"})

    total_activity = sum(r["duration"] for r in records)
    total_water = sum(r["water_intake"] for r in records)
    avg_sleep = sum(r["sleep_hours"] for r in records) / len(records)

    summary = {
        "total_activity_minutes": total_activity,
        "total_water_ml": total_water,
        "average_sleep_hours": round(avg_sleep, 2),
    }

    return jsonify(summary)


if __name__ == "__main__":
    app.run(debug=True)
