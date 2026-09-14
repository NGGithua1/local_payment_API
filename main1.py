from fastapi import FastAPI

# creates the API application.
app = FastAPI(
    title= "local_payment_api",
    version= "1.0.0"
)


@app.get("/") # When someone sends a GET request to /, execute the function below it.
def root(): # Defines what happens when that request arrives.
    return{ # The response will be automatically converted into JSON by FastAPI.
        "service": "local_payment_api",
        "status": "running"
    }