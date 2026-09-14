from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional
import uuid


# -----------------------------
# FastAPI Application
# -----------------------------

app = FastAPI(
    title="local_payment_API",
    version="1.0.0"
)


# -----------------------------
# Authentication Configuration
# -----------------------------

security = HTTPBearer()

# Mock authentication token.
VALID_TOKEN = "test_token_123"


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
# Authentication
# -----------------------------

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Verify that the client supplied the correct Bearer token.
    """

    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )

    return credentials.credentials


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

@app.post("/v1/payments", status_code=201)
def create_payment(
    payment: PaymentRequest,
    token: str = Depends(verify_token)
):
    """
    Create a mock payment after successful authentication.
    """

    transaction_id = f"txn_{uuid.uuid4().hex[:12]}"

    return {
        "transaction_id": transaction_id,
        "status": "successful",
        "amount": payment.amount,
        "currency": payment.currency,
        "reference": payment.reference
    }