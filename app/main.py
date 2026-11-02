from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.config.settings import settings
from app.routers import product_routes

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(product_routes.router)

@app.get("/health", tags=["Health"])
def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy", "service": settings.app_name})
