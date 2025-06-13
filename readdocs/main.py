import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from readdocs.api.routers import include_routers
from readdocs.settings import Settings

app = FastAPI(title="ReadDocs API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(Settings.ALLOW_ORIGINS),  # Convert set to list
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hc():
    return {"error": False, "msg": "Ok", "result": {"status": "SERVING"}}

include_routers(app)

if __name__ == "__main__":
    uvicorn.run("readdocs.main:app", host="0.0.0.0", port=Settings.SERVICE_PORT, reload=Settings.DEBUG, loop="asyncio")