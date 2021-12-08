from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Chefs Academy notification api", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/", status_code=200)
async def root():
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

app.include_router(api_router)