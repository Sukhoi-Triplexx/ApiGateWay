from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
import pandas as pd
import os
import uvicorn
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Tables created")
    yield
    await delete_tables()
    print("Tables deleted")


app = FastAPI(lifespan=lifespan)
@app.get("/")

class STaskAdd(BaseModel):

    name: str
    description: str | None = None

@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes = True)

@app.post("/")
async def add_task(task: STaskAdd = Depends()):
    return {"data": task}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)





