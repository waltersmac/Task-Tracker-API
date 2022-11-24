import fastapi
from fastapi import templating

@app.get("/")
async def root():
    templating.Jinja2Templates(directory="templates")
    return {"message": "Hello World"}