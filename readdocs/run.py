import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from docmintservice.api.routers import include_routers
from docmintservice.settings import Settings

app = FastAPI(title="Docmint API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Settings.ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/")
async def hc():
    return {"error": False, "msg": "Ok", "result": {"status": "SERVING"}}


include_routers(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=Settings.SERVICE_PORT, reload=Settings.DEBUG, loop="asyncio", )