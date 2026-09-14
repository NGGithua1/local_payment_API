from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI(
    title="Mock Payment API",
    version="1.0.0"
)

security = HTTPBearer()

VALID_TOKEN = "test_token_123"

# In-memory transaction storage.
# Key   = transaction_id
# Value = transaction details
transactions = {}


class Customer(BaseModel):
    phone: str


class PaymentRequest(BaseModel):
    amount: float
    currency: str
    customer: Customer
    reference: str
    description: Optional[str] = None


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )

    return credentials.credentials


@app.get("/")
def root():
    return {
        "service": "local_payment_api",
        "status": "running"
    }


@app.post("/v1/payments", status_code=201)
def create_payment(
    payment: PaymentRequest,
    token: str = Depends(verify_token)
):
    transaction_id = f"txn_{uuid.uuid4().hex[:12]}"

    transaction = {
        "transaction_id": transaction_id,
        "status": "successful",
        "amount": payment.amount,
        "currency": payment.currency,
        "customer": payment.customer.model_dump(),
        "reference": payment.reference,
        "description": payment.description
    }

    # Store the transaction in memory
    transactions[transaction_id] = transaction

    return transaction


@app.get("/v1/payments/{transaction_id}")
def get_payment(
    transaction_id: str,
    token: str = Depends(verify_token)
):
    transaction = transactions.get(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction