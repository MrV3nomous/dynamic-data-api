from fastapi import FastAPI, UploadFile, File
from core.data_engine import DataEngine
import pandas as pd
import io

app = FastAPI()

engine = DataEngine()


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/load")
def load_dataset(dataset: dict):
    return engine.load_dataset(dataset)


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.StringIO(content.decode()))
    engine.df = df
    return {
        "status": "success",
        "records": len(df),
        "fields": list(df.columns)
    }


@app.get("/fields")
def fields():
    return engine.get_fields()


@app.get("/records")
def records(limit: int = None):
    return engine.get_records(limit)


@app.get("/stats/{field}")
def stats(field: str):
    return engine.get_stats(field)


@app.get("/filter")
def filter_records(field: str, value: str):
    return engine.filter_records(field, value)


@app.get("/summary")
def summary():
    return engine.dataset_summary()


@app.get("/dataset-info")
def dataset_info():
    return engine.dataset_info()


@app.get("/correlations")
def correlations():
    return engine.correlations()

@app.get("/profile")
def profile():
    return engine.profile_dataset()
