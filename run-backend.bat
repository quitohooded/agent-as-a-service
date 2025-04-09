@echo off
cd backend
echo Iniciando FastAPI en http://localhost:8000 ...
uvicorn main:app --reload
pause
