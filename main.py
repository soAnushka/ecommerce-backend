from fastapi import FastAPI
from routes import product_routes, order_routes

app = FastAPI(
    title="E-commerce Backend",
    description="A sample backend for HROne Internship task using FastAPI + MongoDB",
    version="1.0.0"
)

# Include routes
app.include_router(product_routes.router)
app.include_router(order_routes.router)

# Optional root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Backend!"}
