import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

from dotenv import load_dotenv

# HINT: that's correct - as it's launched from above folder (via `langchain serve`)
load_dotenv("../.env", override=True)
print(f" ***** OPENAI_API_BASE: {os.environ['OPENAI_API_BASE']}")

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


from app.rag import qa
add_routes(app, qa, path="/codechat")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
