import math

import httpx
from fastapi import APIRouter
from services.customers import CustomerService
from werkzeug.exceptions import HTTPException

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/ingest")
async def ingest_customers():
    async with httpx.AsyncClient() as client:

        first_res = await client.get("http://flask:5000/api/customers/?page=1&limit=10")
        first     = first_res.json()
        total     = first["total"]
        pages     = math.ceil(total / 10)

        all_customers = []
        for page in range(1, pages + 1):
            res  = await client.get(f"http://flask:5000/api/customers/?page={page}&limit=10")
            all_customers.extend(res.json()["data"])

        for customer in all_customers:
            CustomerService.create_customer(customer)

    return {"status": "success", "records_processed": len(all_customers)}

@router.get("/")
def read_customers(page: int = 1, limit: int = 10):
    return CustomerService.get_customers(page=page, limit=limit)

@router.get("/{customer_id}")
def read_customer(customer_id: str):
    customer = CustomerService.get_customer_by_id(customer_id)
    
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return customer