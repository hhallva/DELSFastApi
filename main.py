from fastapi import FastAPI
from routes.locations import router as locations_router
from routes.enpoints import router as endpoints_router
from routes.devices import router as device_router
from core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="API для отслеживания местоположения и точек назначения",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(locations_router, prefix="/locations", tags=["locations"])
app.include_router(endpoints_router, prefix="/endpoints", tags=["endpoints"])
app.include_router(device_router   , prefix="/devices"  , tags=["devices"  ])


@app.get("/")
async def root():
    return {
        "message": "Location Tracking API"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
