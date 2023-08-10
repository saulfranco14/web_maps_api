from fastapi                        import FastAPI
from fastapi.middleware.cors        import CORSMiddleware
from src.routes.users.main          import router as UserRouter

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["Usuarios"], prefix="/user")

@app.get("/", tags=["Root"])
async def read_root():
    return{
        "message" : "Web Maps API"
    }