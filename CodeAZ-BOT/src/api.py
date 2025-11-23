from fastapi import FastAPI
import json
from path import XP_JSON

app = FastAPI()

@app.get("/xp/{user_id}")
def get_xp(user_id: int):
    with open(XP_JSON, "r", encoding="utf-8") as f:
        xp_data = json.load(f)

    return {
        "user_id": user_id,
        "xp": xp_data.get(str(user_id), 0)
    }