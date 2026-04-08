import os
import json
import hashlib
from pathlib import Path

INDEX_META_PATH = "data/index/index_meta.json"

def file_sha256(file_path: str) -> str:
    content = Path(file_path).read_bytes()
    return hashlib.sha256(content).hexdigest()

def build_index_meta(data_dir: str, chunk_size: int, overlap: int) -> dict:
    files = sorted(
        [f for f in os.listdir(data_dir) if f.endswith(".txt")]
    )

    file_hashes = {}
    for file_name in files:
        file_path = os.path.join(data_dir, file_name)
        file_hashes[file_path] = file_sha256(file_path)

    return {
        "files": file_hashes,
        "chunk_size": chunk_size,
        "overlap": overlap
    }

def load_saved_meta() -> dict | None:
    if not os.path.exists(INDEX_META_PATH):
        return None

    try:
        with open(INDEX_META_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return None
            return json.loads(content)
    except json.JSONDecodeError:
        return None

def save_meta(meta: dict) -> None:
    with open(INDEX_META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

def should_rebuild_index(current_meta:dict) -> bool:
    saved_meta = load_saved_meta()
    if saved_meta is None:
        return True
    return saved_meta != current_meta