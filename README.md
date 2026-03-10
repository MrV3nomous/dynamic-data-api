# Dynamic Data Analytics API

A versatile backend API built with FastAPI and Flask that allows you to dynamically load JSON or CSV datasets, explore fields, get stats, correlations, and automatic profiling. Perfect for data inspection, analytics, and testing.

---

## 🔹 Features

- Load datasets dynamically from JSON or CSV
- Explore fields, records, numeric & text columns
- Get statistics (mean, min, max) on numeric fields
- Filter records by field values
- Compute correlations between numeric fields
- Generate automatic data profiles for all columns
- Supports FastAPI and Flask, demonstrating framework comparison
- Graceful handling of bad inputs or missing fields

---

## Installation

#### Clone the repo:

```bash
git clone https://www.github.com/MrV3nomous/dynamic-data-api/
cd dynamic-data-api
```

#### Install dependencies:

```bash
pip install -r requirements.txt
```

#### Run FastAPI:

```bash
uvicorn fastapi_server.main:app --reload
```

Or Flask:

```bash
python flask_server/main.py
```

---

## 🧪 Testing the API

#### 1. FastAPI Swagger UI

```bash
http://127.0.0.1:8000/docs
```

Interact with all endpoints easily.


#### 2. Health Check

```bash
GET /health
```

Response:

```bash
{"status": "running"}
```

#### 3. Load JSON Dataset

```bash
POST /load
```

##### Sample body:

```bash
{
  "data": [
    {"item": "Apple", "category": "Fruit", "price": 1.2, "stock": 120, "demand": 80},
    {"item": "Banana", "category": "Fruit", "price": 0.8, "stock": 200, "demand": 150}
  ]
}
```

#### 4. Upload CSV

```bash
POST /upload-csv
```

Upload your CSV directly.

Example CSV:

```bash
item,category,price,stock,demand
Apple,Fruit,1.2,120,80
Banana,Fruit,0.8,200,150
```

#### 5. Explore Fields & Records

```bash
GET /fields
GET /records
GET /summary
GET /dataset-info
```

#### 6. Analytics

```bash
GET /stats/{field}        # Stats for a numeric field
GET /filter?field=X&value=Y
GET /correlations          # Correlations of numeric fields
GET /profile               # Automatic profiling of all columns
```

---


## 📊 Sample Workflow

- Load JSON/CSV
- Check /fields
- Inspect /summary
- Get stats /stats/price
- Filter /filter?field=category&value=Fruit
- Compute correlations /correlations
- View automatic profiling /profile


---


## 💡 Testing Tips

- Use Swagger UI (FastAPI) for interactive requests
- Take screenshots for GitHub README (fields, summary, profile)
- Test both JSON and CSV uploads
- Check error handling by sending missing fields or bad data


## 📌 Technologies Used

- Python 3.11+
- FastAPI — Modern, async-ready API framework
- Flask — Lightweight, beginner-friendly API framework
- Pandas — Powerful data handling and analysis
- Python standard libraries


---


## 📦 Installation & Run Summary

```bash
git clone <repo-url>
pip install -r requirements.txt
uvicorn fastapi_server.main:app --reload   # FastAPI
python flask_server/main.py                # Flask
```

Test with:

```bash
JSON: /load
CSV: /upload-csv
```

Explore & analyze with
```bash
/fields, /summary, /stats/{field}, /filter, /correlations, /profile
```

## 📄 License
MIT License – See LICENSE

