from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.investment import router as investment_router


app = FastAPI()
app.include_router(investment_router)
origins = [
    "http://localhost:8000", # back
    "http://localhost:4200", # front
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
