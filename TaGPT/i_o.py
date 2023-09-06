import pandas as pd
from utils.logger import log_pipeline


@log_pipeline
def load_data(data_path: str) -> list[dict]:
    if not data_path.endswith(".xlsx"):
        raise ValueError("Only supports .xlsx files for now")
    return pd.read_excel(data_path).to_dict(orient="records")


@log_pipeline
def save_data(data: list[dict], save_path: str) -> None:
    df = pd.DataFrame(
        {
            "Material description": [d["Material description"] for d in data],
            "Industry Std Desc.": [d["Industry Std Desc."] for d in data],
            "tags": [d["tags"] for d in data],
        }
    )

    df.to_csv(save_path, index=False)
