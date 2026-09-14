from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid


app = FastAPI(
    title="local_payment_api",
    version="1.0.0"
)


# -----------------------------
# Request Models
# -----------------------------

class Customer(BaseModel):
    phone: str


class PaymentRequest(BaseModel):
    amount: float
    currency: str
    customer: Customer
    reference: str
    description: Optional[str] = None


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
def root():
    return {
        "service": "local_payment_api",
        "status": "running"
    }


# -----------------------------
# Create Payment
# -----------------------------

@app.post("/v1/payments")
def create_payment(payment: PaymentRequest):

    transaction_id = f"txn_{uuid.uuid4().hex[:12]}"

    return {
        "transaction_id": transaction_id,
        "status": "successful",
        "amount": payment.amount,
        "currency": payment.currency,
        "reference": payment.reference
    }