from flask import Flask, request, jsonify
from models import HealthRecord
from storage import load_data, save_data

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "HealthyLife Tracker is running"}


@app.post("/add")
def add_record():
    data = request.json  # 从客户端获取 JSON 数据

    record = HealthRecord(
        date=data["date"],
        activity=data["activity"],
        duration=data["duration"],
        water_intake=data["water_intake"],
        sleep_hours=data["sleep_hours"]
    )

    # 读取现有数据
    records = load_data()

    # 将新数据转换为字典并追加
    records.append(record.__dict__)

    # 保存数据
    save_data(records)

    return jsonify({"status": "success", "message": "Record added!"})


if __name__ == "__main__":
    app.run(debug=True)
