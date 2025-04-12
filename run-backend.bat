@echo off
cd backend
echo Activando entorno virtual...
call ..\.venv\Scripts\activate.bat
echo Iniciando FastAPI en http://localhost:8000 ...
uvicorn main:app --reload
pause