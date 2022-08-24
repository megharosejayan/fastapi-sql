from fastapi import FastAPI

from server.routes.sequence import router as SequenceRouter

app = FastAPI()

app.include_router(SequenceRouter, tags=["Sequence"], prefix="/sequence")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome :)"}
    