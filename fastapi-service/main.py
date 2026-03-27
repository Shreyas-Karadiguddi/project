from api.customers.endpoint import router as customers_router
from config import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customers_router, prefix="/api")
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

print("FASTAPI IS RUNNING")
