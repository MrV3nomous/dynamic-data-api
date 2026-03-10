import pandas as pd


class DataEngine:

    def __init__(self):
        self.df = None

    def check_loaded(self):
        return self.df is not None

    def load_dataset(self, dataset):

        if "data" not in dataset:
            return {"status": "error", "message": "Missing 'data' key"}

        data = dataset["data"]

        if not isinstance(data, list) or len(data) == 0:
            return {"status": "error", "message": "Dataset must contain records"}

        self.df = pd.DataFrame(data)

        return {
            "status": "success",
            "records": len(self.df),
            "fields": list(self.df.columns)
        }

    def load_csv(self, file):

        try:
            self.df = pd.read_csv(file)
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return {
            "status": "success",
            "records": len(self.df),
            "fields": list(self.df.columns)
        }

    def get_fields(self):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        return {
            "status": "success",
            "fields": list(self.df.columns)
        }

    def get_records(self, limit=None):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        if limit:
            records = self.df.head(limit).to_dict(orient="records")
        else:
            records = self.df.to_dict(orient="records")

        return {
            "status": "success",
            "records": records
        }

    def get_stats(self, field):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        if field not in self.df.columns:
            return {
                "status": "error",
                "message": "Field not found",
                "available_fields": list(self.df.columns)
            }

        if not pd.api.types.is_numeric_dtype(self.df[field]):
            return {"status": "error", "message": "Field is not numeric"}

        return {
            "status": "success",
            "field": field,
            "mean": float(self.df[field].mean()),
            "min": float(self.df[field].min()),
            "max": float(self.df[field].max())
        }

    def filter_records(self, field, value):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        if field not in self.df.columns:
            return {"status": "error", "message": "Field not found"}

        results = self.df[self.df[field].astype(str) == str(value)]

        return {
            "status": "success",
            "results": results.to_dict(orient="records")
        }

    def dataset_summary(self):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        numeric = self.df.select_dtypes(include="number").columns.tolist()
        text = self.df.select_dtypes(exclude="number").columns.tolist()

        return {
            "status": "success",
            "records": len(self.df),
            "fields": list(self.df.columns),
            "numeric_fields": numeric,
            "text_fields": text
        }

    def dataset_info(self):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        numeric = self.df.select_dtypes(include="number").columns.tolist()
        text = self.df.select_dtypes(exclude="number").columns.tolist()

        return {
            "status": "success",
            "records": len(self.df),
            "field_count": len(self.df.columns),
            "numeric_fields": numeric,
            "text_fields": text
        }

    def correlations(self):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:
            return {
                "status": "error",
                "message": "Not enough numeric fields for correlation"
            }

        corr = numeric_df.corr()

        return {
            "status": "success",
            "correlations": corr.to_dict()
        }

    def profile_dataset(self):

        if not self.check_loaded():
            return {"status": "error", "message": "Dataset not loaded"}

        profile = {}

        for column in self.df.columns:

            col = self.df[column]

            if pd.api.types.is_numeric_dtype(col):

                profile[column] = {
                    "type": "numeric",
                    "mean": float(col.mean()),
                    "min": float(col.min()),
                    "max": float(col.max()),
                    "missing": int(col.isna().sum())
                }

            else:

                profile[column] = {
                    "type": "text",
                    "unique_values": int(col.nunique()),
                    "missing": int(col.isna().sum())
                }

        return {
            "status": "success",
            "profile": profile
        }
