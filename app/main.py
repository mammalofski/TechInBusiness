from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from pathlib import Path

app = FastAPI(title="TechInBusiness")

# Mount static files
static_path = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Templates
templates = Jinja2Templates(directory=str(static_path))

class ContactForm(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    service: str
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/book-service")
async def book_service(contact: ContactForm):
    # Here you would typically:
    # 1. Save to database
    # 2. Send email notification
    # 3. Process the booking
    
    # For now, we'll just return a success response
    return {"status": "success", "message": "Thank you for your interest! We'll contact you soon."}