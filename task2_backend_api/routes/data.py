from fastapi import APIRouter, Depends
from utils import get_current_user, require_role
import pandas as pd

router = APIRouter()
data = pd.read_csv("processed_data.csv")

@router.get("/data")
def get_data(current_user = Depends(get_current_user)):
    """Return 10 random records from the dataset"""
    return data.sample(10).to_dict(orient="records")

@router.get("/admin/data")
def get_admin_data(current_user = Depends(require_role("admin"))):
    """Return dataset summary for admin users only"""
    return {
        "row_count": len(data),
        "columns": list(data.columns),
        "missing": data.isnull().sum().to_dict()
    }
