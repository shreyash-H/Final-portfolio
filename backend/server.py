from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging
from pathlib import Path
import uuid
from typing import Dict, Any
try:
    from motor.motor_asyncio import AsyncIOMotorClient
except Exception:
    AsyncIOMotorClient = None

ROOT_DIR = Path(__file__).parent
# load .env from backend folder if present
load_dotenv(ROOT_DIR / '.env')

app = FastAPI(title="Deploy-Ready Backend", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("backend")

# Simple storage (in-memory fallback if no MONGO_URI)
MONGO_URI = os.environ.get("MONGO_URI")
client = None
db = None
COLLECTION = "items"

if MONGO_URI and AsyncIOMotorClient is not None:
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client.get_default_database()
        logger.info("Connected to MongoDB")
    except Exception as e:
        logger.warning("Could not connect to MongoDB, falling back to in-memory store: %s", e)

_memory_store: Dict[str, Dict[str, Any]] = {}

@app.on_event("shutdown")
async def shutdown_db_client():
    if client:
        client.close()
        logger.info("Mongo client closed")

@app.get("/health")
async def health():
    return {"status": "ok", "time": __import__('datetime').datetime.now().isoformat()}

@app.post("/items")
async def create_item(payload: dict):
    """Create an item. If Mongo is configured, save there; otherwise use memory."""
    item_id = str(uuid.uuid4())
    payload.update({"id": item_id, "created_at": __import__('datetime').datetime.now().isoformat()})
    if db:
        # async insert to Mongo
        res = await db[COLLECTION].insert_one(payload)
        payload["_mongo_id"] = str(res.inserted_id)
        return payload
    else:
        _memory_store[item_id] = payload
        return payload

@app.get("/items")
async def list_items():
    if db:
        docs = await db[COLLECTION].find().to_list(length=100)
        return docs
    else:
        return list(_memory_store.values())

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if db:
        doc = await db[COLLECTION].find_one({"id": item_id})
        if not doc:
            raise HTTPException(status_code=404, detail="Item not found")
        return doc
    else:
        item = _memory_store.get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if db:
        res = await db[COLLECTION].delete_one({"id": item_id})
        if res.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"deleted": True}
    else:
        if item_id in _memory_store:
            del _memory_store[item_id]
            return {"deleted": True}
        raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)
