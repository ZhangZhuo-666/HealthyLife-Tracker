# HealthyLife Tracker — IWM2 Final Submission

HealthyLife Tracker is a simple health tracking application developed for IWM1 + IWM2.

## How to Run Locally

```bash
pip install flask
python src/app.py
```

The server will run at:
http://127.0.0.1:5000

## Run Tests

```bash
pytest
```

## Run with Docker

Build the Docker image:

```bash
docker build -t health-tracker .
```

Run the container:

```bash
docker run -p 5000:5000 health-tracker
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /add | Add a new health record |
| GET | /records | Retrieve all records |
| GET | /weekly-summary | Weekly summary calculation |

## Project Structure

```
HealthyLife-Tracker/
├── src/
│   ├── app.py
│   ├── models.py
│   └── storage.py
├── tests/
│   └── test_basic.py
├── Dockerfile
├── .github/workflows/ci.yml
├── screenshots/
└── README.md
```

## IWM2 Requirements Completed

- Core features implemented
- Unit + integration testing
- CI pipeline (GitHub Actions)
- Docker containerization
- Documentation + README
- Screenshots folder prepared
- Demo-ready application
