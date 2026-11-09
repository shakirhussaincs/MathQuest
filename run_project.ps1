# PowerShell script to start MathQuest backend and frontend
# -------------------------------------------------------
# 1. Activate virtual environment
$venv = "d:\\mathQuest\\.venv\\Scripts\\Activate.ps1"
if (Test-Path $venv) {
    Write-Host "Activating virtual environment..."
    & $venv
} else {
    Write-Error "Virtual environment not found at $venv"
    exit 1
}

# 2. Set PYTHONPATH so that `app` package is found (backend folder)
$env:PYTHONPATH = "d:\\mathQuest\\backend"
Write-Host "PYTHONPATH set to $env:PYTHONPATH"

# 3. Start backend (FastAPI) in a new background job
Write-Host "Starting FastAPI backend..."
$backendJob = Start-Job -ScriptBlock {
    d:\\mathQuest\\.venv\\Scripts\\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
}
# Give backend a few seconds to start
Start-Sleep -Seconds 5

# 4. Start frontend (Vite) in a new PowerShell window
Write-Host "Starting React frontend..."
Start-Process "powershell.exe" -ArgumentList "-NoProfile -Command \"cd 'd:\\mathQuest\\frontend'; npm run dev\""

Write-Host "Both services should be running now."
Write-Host "Backend: http://localhost:8000"
Write-Host "Frontend: http://localhost:5173"

