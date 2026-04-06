import json
import os
from typing import List, Dict, Any

INDEX_PATH = "data/index.json"

def save_index(index: List[Dict[str, Any]]):
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f)

def load_index() -> List[Dict[str, Any]]:
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def index_exists() -> bool:
    return os.path.exists(INDEX_PATH)