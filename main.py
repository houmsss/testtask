from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root(name, message):
    html = f"<p>Hello {name}! <br> {message}</p>"
    return HTMLResponse(content=html)
