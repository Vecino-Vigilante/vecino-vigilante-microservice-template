from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .infrastructure.docs.openapi_tags import openapi_tags
from .infrastructure.routers.management_router import management_router

load_dotenv()

app = FastAPI(
    title=getenv("MICROSERVICE_NAME"),
    summary=getenv("MICROSERVICE_SUMMARY"),
    version=getenv("MICROSERVICE_VERSION"),
    contact={
        "name": getenv("MICROSERVICE_DEVELOPER"),
        "email": getenv("MICROSERVICE_DEVELOPER_EMAIL"),
    },
    openapi_tags=openapi_tags,
)

app.include_router(management_router, prefix="/management", tags=["Management"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
