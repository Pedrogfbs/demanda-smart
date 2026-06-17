from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn

# =========================
# APP
# =========================
app = FastAPI(
    title="Demand Smart",
    version="2.0.0"
)

# =========================
# BASE DIR (EVITA ERROS DE CAMINHO)
# =========================
BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

# =========================
# STATIC FILES
# =========================
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# =========================
# JINJA TEMPLATES
# =========================
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# =========================
# DASHBOARD (WEB)
# =========================
@app.get("/")
def dashboard(request: Request):

    dashboard_file = TEMPLATES_DIR / "dashboard.html"

    # 🔥 DEBUG SE DER ERRO
    if not dashboard_file.exists():
        return JSONResponse({
            "erro": "dashboard.html não encontrado",
            "caminho_esperado": str(dashboard_file)
        })

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


# =========================
# STATUS API
# =========================
@app.get("/status")
def status():
    return {
        "api": "online",
        "versao": "2.0.0"
    }


# =========================
# DASHBOARD API (JSON)
# =========================
@app.get("/dashboard")
def dashboard_api():
    return {
        "demanda_atual_kw": 205,
        "potencia_disponivel_kw": 95,
        "quantidade_pivos": 4,
        "pivos_ligados": ["Pivô 1", "Pivô 2"]
    }


# =========================
# ANUAL API
# =========================
@app.get("/dashboard-anual")
def dashboard_anual():
    return {
        "consumo_mensal": [
            12000, 14000, 13500, 16000,
            18000, 21000, 24000, 23000,
            19500, 17000, 15000, 13000
        ]
    }


# =========================
# PÁGINAS WEB
# =========================
@app.get("/pivos")
def pivos(request: Request):
    return templates.TemplateResponse("pivos.html", {"request": request})


@app.get("/manutencao")
def manutencao(request: Request):
    return templates.TemplateResponse("manutencao.html", {"request": request})


@app.get("/relatorios")
def relatorios(request: Request):
    return templates.TemplateResponse("relatorios.html", {"request": request})


@app.get("/financeiro")
def financeiro(request: Request):
    return templates.TemplateResponse("financeiro.html", {"request": request})


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )