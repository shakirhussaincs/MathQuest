# Vercel FastAPI entry‑point wrapper
# Exposes the FastAPI `app` instance that lives in `backend/app/main.py`
# Vercel's FastAPI framework expects a top‑level module named `app`.

from app.main import app  # re‑export for Vercel

