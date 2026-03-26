import httpx
from fastapi import APIRouter
from services.customers import CustomerService

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/ingest")
async def get_customers():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://flask:5001/api/customers/")
        customers = response.json()
        for customer in customers:
            CustomerService.create_customer(customer)
    return {"message": "Customers ingested successfully"}

@router.get("/")
def read_customers():
    return CustomerService.get_customers()