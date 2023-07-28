from fastapi import FastAPI
from . import models
from .routes import router

app = FastAPI()

models.Base.metadata.create_all(bind=models.engine)

app.include_router(router)
